#Sample of code, taking an extract file and formatting it.

import pandas as pd
import tabula
import os
from urllib.parse import unquote
from datetime import datetime

#Path to File
file_path = "Extract File.XLS"

#Excel File to Dataframe
df = pd.read_excel('Extract File.XLS')

#Delete rows 1 through 29
df = df.iloc[28:]

#Delete columns A, B, and C
df = df.drop(df.columns[[0, 1, 2]], axis=1)

#Delete / in row 1
df.iloc[0] = df.iloc[0].str.replace("/", "", regex=False)

#Delete - in row 1
df.iloc[0] = df.iloc[0].str.replace("-", "", regex=False)

#Replace # with empty string in row 1
df.iloc[0] = df.iloc[0].str.replace("#", "Number", regex=False)

#Replace # with empty string in row 1
df.iloc[0] = df.iloc[0].str.replace("&", "and", regex=False)

#Replace spaces with _ in row 1
df.iloc[0] = df.iloc[0].str.replace(' ', '_', regex=False)

#Delete dots in row 1
df.iloc[0] = df.iloc[0].str.replace(".", "", regex=False)

#Replace + in row 1
df.iloc[0] = df.iloc[0].str.replace("+", "PLUS", regex=False)

#Delete ( in row 1
df.iloc[0] = df.iloc[0].str.replace("(", "", regex=False)

#Delete ) in row 1
df.iloc[0] = df.iloc[0].str.replace(")", "", regex=False)

#Rename the columns with the modified row 1 values
df = df.rename(columns=dict(zip(df.columns, df.iloc[0])))

#Delete all columns after "Most_Relevant_Consol"
df = df.iloc[:, :df.columns.get_loc('Most_Relevant_Consol')+1]

#Delete the modified row 1
df = df.drop(df.index[0])

#Delete all rows for column #1 that are blank
df = df.dropna(subset=[df.columns[0]])

#Save the modified dataframe to a new CSV file
df.to_csv("Job_Profit_Analysis", index=False)

#Convert coolumns to datetime
df['Opened'] = pd.to_datetime(df['Opened'], format='%Y-%m-%d %H:%M:%S')
df['Recognized'] = pd.to_datetime(df['Recognized'], format='%Y-%m-%d %H:%M:%S')

#Convert columns to Float64
df['Revenue'] = df['Revenue'].astype(float)
df['WIP'] = df['WIP'].astype(float)
df['Cost'] = df['Cost'].astype(float)
df['Accrual'] = df['Accrual'].astype(float)
df['Job_Profit'] = df['Job_Profit'].astype(float)

print(df.columns)
