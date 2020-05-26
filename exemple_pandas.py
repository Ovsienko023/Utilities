import pandas as pd
import numpy


name_file = 'test.xlsx'

file_2 = pd.read_excel(name_file, sheet_name='1')

for i in file_2.values:
    print(i)

a = file_2.values[12]
arr = numpy.array(a)
for i in arr:
    print(i)
