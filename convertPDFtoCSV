#The following code's purpose is to do the following:
#(1) Takes a PDF file, and formats it to a proper format (such as proper date format for certain columns)
#(2) This PDF file is appended to a historical data file, that stores the same information
#Note --- this code was based off a specific format, as the PDF file is an exported report.


import pandas as pd
import tabula
import os
from urllib.parse import unquote
from datetime import datetime

#Replace this with the path to your PDF file
file_path = "PDF NAME.pdf"

#Read PDF and convert to DataFrame
dfs = tabula.read_pdf(file_path, pages='all')

#Concatenate all DataFrames
df = pd.concat(dfs)

#Drop first column
df = df.iloc[:, 0:]

#Format column headers - Converts #_Mo or ##_Mo to mm/dd/yyyy, replaces spaces in column headers with _
for i, col in enumerate(df.columns):
    if col[0].isdigit():
        new_date_col = datetime.strptime(col, '%d %b').strftime('%m/%d/%Y')
        new_date_col = new_date_col[:-4] + str(datetime.now().year)
        df = df.rename(columns={col: new_date_col})
    else:
        df = df.rename(columns={col: col.replace(' ', '_')})

#Convert DataFrame to CSV
df.to_csv("PDF TO CSV", index=False)

#Load Container Heating Report and new PDF Container Heating Report into DataFrames
fileA_path = 'HISTORICAL FILE TO APPEND TO'
fileB_path = 'PDF TO CSV'
fileA = pd.read_csv(fileA_path)
fileB = pd.read_csv(fileB_path)

#Perform the merge on the 'Container' column
merged = pd.merge(fileA, fileB, on='Container', how='left', suffixes=('_A', '_B'))

#Get columns from FileB that are not present in FileA
columns_to_add = [col for col in fileB.columns if col not in fileA.columns]

#Create a new DataFrame with columns from FileA
final_df = fileA.copy()

#Merge columns from FileB that are not present in FileA
for col in columns_to_add:
    final_df[col] = merged[col]

#Convert DataFrame to CSV
final_df.to_csv("HISTORICAL FILE TO APPEND TO", index=False)

#Melt the DataFrame to create 'Date_of_Recording' and 'Temperature' columns
id_vars = ['Container', 'Product', 'Amount', 'Desired_Temp.']
final_df = pd.melt(final_df, id_vars=id_vars, var_name='Date_of_Recording', value_name='Temperature')

#Convert 'Date_of_Recording' from string to datetime format
final_df['Date_of_Recording'] = pd.to_datetime(final_df['Date_of_Recording'], format='%m/%d/%Y')

#Sort the DataFrame by 'Container' and 'Date_of_Recording'
final_df = final_df.sort_values(by=['Container', 'Date_of_Recording'])

#Count the number of zeroes/nulls/blanks
final_df['Count_of_Zero_Temperatures'] = final_df['Temperature'].apply(lambda x: 1 if pd.isnull(x) or x == 0 else 0)

#Reset the index of the DataFrame
final_df.reset_index(drop=True, inplace=True)

#Save the DataFrame to a new CSV file
output_file_path = 'SAVED FILE'
final_df.to_csv(output_file_path, index=False)
