import pandas as pd
"""
http://pandas.pydata.org/pandas-docs/stable/io.html#io-read-csv-table
"""
data = pd.read_csv('student.csv')
print(data)
data.to_pickle('student.pickle')
