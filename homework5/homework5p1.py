#Hans Vos
#1003181
#CS 10 Tue Thur
#DUE final exam
import pandas as pd
from io import StringIO

# makes it easy to read globs of text like the data you posted above
Tea_data = StringIO('''Green Tea:8580.0:7201.25:8900.0
Earl Grey:10225.25:9025.0:9505.0
Ceylon:6700.1:5012.45:6011.0
Jasmine:9285.15:8276.1:8705.0
Mint Tea:7901.25:4267.0:7056.5''')

pdf = pd.read_csv(Tea_data, sep = ':', header = None)

# returns a list of column names from the string you have above
pdf.columns = "tea_name:store1_Sales:store2_Sales:store3_Sales".split(':')

# add up the sales for stores 1, 2, and 3 for each type of tea to get total sales for a given tea
pdf['total_sales'] = pdf[['store1_Sales', 'store2_Sales', 'store3_Sales']].sum(axis = 1)
print(pdf)
# print('Amount paid for the stock:          $ ' + format(numberOfShares*purchasePrice, ',.2f'))


# Hanss-MacBook-Pro:homework5 hansvos$ python homework5p1.py
#     tea_name  store1_Sales  store2_Sales  store3_Sales  total_sales
# 0  Green Tea       8580.00       7201.25        8900.0     24681.25
# 1  Earl Grey      10225.25       9025.00        9505.0     28755.25
# 2     Ceylon       6700.10       5012.45        6011.0     17723.55
# 3    Jasmine       9285.15       8276.10        8705.0     26266.25
# 4   Mint Tea       7901.25       4267.00        7056.5     19224.75
