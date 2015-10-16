"""
we have read in our excel file using pd.read_excel(io, sheetname='somename', index_col='colname')

import pandas as pd

Read excel file name d SuperstoreSales.xlsx

create a logical file name
fn = 'C:/myPy/SuperstoreSales.xlsx'

Read into a data frame

df = pd.read_excel(fn, sheetname='Orders', index_col='Order Date')

print(df)

print(df.head(5))
print(df.tail(10))

Create a group (cluster by) on Ship Mode and compute the Shipping Cost statistics for each mode

ShipCostByMode = df['Shipping Cost'].groupby(df['Ship Mode'])

ShipCostByMode.describe()

ShipCostByMode.mean()

Find those customers having sales greater than $5,000

print(df['Customer Name'].where(df['Sales'] > 5000))
