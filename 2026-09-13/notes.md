# 2026-09-13

## Chu de hom nay
numpy

## Nhung gi da hoc / What I learned
- Hieu ro ve thu vien NumPy: cach tao mang (np.array), cac ham tao mang co san (np.zeros, np.ones, np.arange...), indexing & slicing tren mang 1 chieu va 2 chieu.
  (Gained a clear understanding of the NumPy library: how to create arrays (np.array), built-in array creation functions (np.zeros, np.ones, np.arange...), and indexing & slicing on 1D and 2D arrays.)
- Ket hop Pandas va NumPy de tinh toan gia tien: dung groupby, sum, tinh tong/trung binh gia tri tren du lieu dang bang.
  (Combined Pandas and NumPy to calculate prices: used groupby, sum, and computed totals/averages on tabular data.)
- Ung dung xac suat co ban de du doan kha nang xay ra cua mot su kien dua tren du lieu da co.
  (Applied basic probability concepts to predict the likelihood of an event based on existing data.)

## Code / vi du
```python
import numpy as np
import pandas as pd

# Vi du: tinh tong gia tri don hang
df['total_price'] = df['quantity'] * df['item_price']
tong_gia_tri = df['total_price'].sum()

# Vi du: dung numpy tinh xac suat don gian
# Xac suat = so truong hop thoa man / tong so truong hop
xac_suat = np.mean(df['quantity'] > 1)
print(f"Xac suat don hang co quantity > 1: {xac_suat:.2%}")
```

## Cau hoi con thac mac / Open questions
- no comments