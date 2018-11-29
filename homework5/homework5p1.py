#Hans Vos
#1003181
#CS 10 Tue Thur
#DUE final exams
import pandas as pd
from io import StringIO

# makes it easy to read globs of text like the data you posted above
data = StringIO('''Green Tea:8580.0:7201.25:8900.0
Earl Grey:10225.25:9025.0:9505.0
Ceylon:6700.1:5012.45:6011.0
Jasmine:9285.15:8276.1:8705.0
Mint Tea:7901.25:4267.0:7056.5''')

df = pd.read_csv(data, sep = ':', header = None)

# returns a list of column names from the string you have above
df.columns = "tea_name:store1_Sales:store2_Sales:store3_Sales".split(':')

# add up the sales for stores 1, 2, and 3 for each type of tea to get total sales for a given tea
df['total_sales'] = df[['store1_Sales', 'store2_Sales', 'store3_Sales']].sum(axis = 1)
print(df)
# print('Amount paid for the stock:          $ ' + format(numberOfShares*purchasePrice, ',.2f'))



# dictionary = {}
# tea_file = open('tea.txt', 'r')
# descr = tea_file.readline()
#
# for line in descr:
#     if line != num:
# print(descr)
# split1 = descr.split(':')
#
# # print(descr)
# # total = int(split1[1]) + int(split1[2]) + int(split1[3])
# # print(split1[0], split1[1], split1[2], split1[3], total)
# print(type(split1[1]))
# print(split1[0] + '      ' + format(int(split1[1], ',.2f')))
