@echo off
REM ============================================================
REM  run_daily_push.bat
REM  Double-click file nay de tao note hoc AI hom nay + push GitHub
REM  Dat file .bat nay CUNG THU MUC voi daily_ai_push.py va trong repo git
REM ============================================================

cd /d "%~dp0"
python daily_ai_push.py
pause
