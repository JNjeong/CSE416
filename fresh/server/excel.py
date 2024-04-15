#pip install xlrd
#pip install openpyxl
#pip install pandas

#https://devpouch.tistory.com/196

import pandas as pd

file_name = 'courses.xlsx'

df = pd.read_excel(file_name)
print(df)

df = pd.read_excel(file_name, sheet_name = '1')
print(df)

