"""
daily_ai_push.py
-----------------
Script tu dong hoa viec ghi "nhat ky hoc AI hang ngay" va day len GitHub.

Cach dung:
    python daily_ai_push.py
    python daily_ai_push.py "Hoc ve groupby va value_counts trong pandas"

Yeu cau:
    - Da cai Git va da git clone / git init repo nay tu truoc.
    - Da cau hinh remote origin tro ve GitHub cua ban.
    - Chay script nay ngay trong thu muc goc cua repo (noi co .git).
"""

import subprocess
import sys
from datetime import date
from pathlib import Path

# ====== CAU HINH ======
README_TABLE_MARKER = "<!-- DAILY_LOG_TABLE -->"  # dong danh dau trong README de chen dong moi vao


def run(cmd, cwd=None):
    """Chay 1 lenh shell, in ra ket qua, dung lai neu loi."""
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.returncode != 0:
        print(result.stderr.strip())
        sys.exit(f"Lenh that bai: {' '.join(cmd)}")
    return result.stdout.strip()


def ensure_git_repo(root: Path):
    if not (root / ".git").exists():
        sys.exit("Khong tim thay thu muc .git — hay chay script nay trong repo da git init/clone.")


def create_today_folder(root: Path, topic: str) -> Path:
    today = date.today().isoformat()  # vd: 2026-09-10
    day_folder = root / today
    day_folder.mkdir(exist_ok=True)

    notes_path = day_folder / "notes.md"
    if not notes_path.exists():
        notes_path.write_text(
            f"# {today}\n\n"
            f"## Chu de hom nay\n{topic or '(chua dien)'}\n\n"
            f"## Nhung gi da hoc\n- \n\n"
            f"## Code / vi du\n```python\n\n```\n\n"
            f"## Cau hoi con thac mac\n- \n",
            encoding="utf-8",
        )
        print(f"Da tao {notes_path}")
    else:
        print(f"{notes_path} da ton tai, khong ghi de.")

    return day_folder


def update_readme_index(root: Path, day_folder: Path, topic: str):
    readme_path = root / "README.md"
    today = day_folder.name
    new_row = f"| {today} | {topic or '(chua dien)'} | [Link](./{today}/notes.md) |\n"

    if not readme_path.exists():
        content = (
            "# Daily Learning AI\n\n"
            "Ghi lai qua trinh hoc AI/ML moi ngay.\n\n"
            "## Nhat ky hoc\n"
            "| Ngay | Chu de | Ghi chu |\n"
            "|---|---|---|\n"
            f"{READMEROW_PLACEHOLDER}"
        ).replace("READMEROW_PLACEHOLDER", new_row)
        readme_path.write_text(content, encoding="utf-8")
        print("Da tao README.md moi.")
        return

    text = readme_path.read_text(encoding="utf-8")
    if today in text:
        print("README.md da co dong cho hom nay, bo qua.")
        return

    # Chen dong moi ngay sau dong header cua bang (dong '|---|---|---|')
    lines = text.splitlines(keepends=True)
    inserted = False
    for i, line in enumerate(lines):
        if line.strip().startswith("|---"):
            lines.insert(i + 1, new_row)
            inserted = True
            break
    if not inserted:
        lines.append("\n## Nhat ky hoc\n| Ngay | Chu de | Ghi chu |\n|---|---|---|\n" + new_row)

    readme_path.write_text("".join(lines), encoding="utf-8")
    print("Da cap nhat README.md.")


def git_commit_and_push(root: Path, topic: str):
    today = date.today().isoformat()
    run(["git", "add", "."], cwd=root)

    status = run(["git", "status", "--porcelain"], cwd=root)
    if not status:
        print("Khong co thay doi gi de commit.")
        return

    message = f"Day {today}: {topic}" if topic else f"Day {today}"
    run(["git", "commit", "-m", message], cwd=root)
    run(["git", "push"], cwd=root)
    print("Da push len GitHub thanh cong!")


def main():
    root = Path(__file__).resolve().parent
    ensure_git_repo(root)

    topic = " ".join(sys.argv[1:]).strip()
    if not topic:
        topic = input("Chu de hoc hom nay (Enter de bo qua): ").strip()

    day_folder = create_today_folder(root, topic)
    update_readme_index(root, day_folder, topic)
    git_commit_and_push(root, topic)


if __name__ == "__main__":
    main()
