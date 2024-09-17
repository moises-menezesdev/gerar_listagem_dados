# Missing Data Report Script
This Python script reads an Excel file containing user data, identifies any missing information in the records, and saves a report of the missing data to a text file. It uses the pandas library to handle the Excel file and to process the data.

Requirements:

Python 3.x
pandas library
Setup:

Install the pandas library by running:
pip install pandas

Usage:
1° Modify the path in the pd.read_excel() function to point to your Excel file.
2° Ensure the column names in the script match those in your Excel file:

NOME for the name column
3° Run the script using Python:
python script.py

Functionality:
1° Reads the Excel file into a DataFrame.
2° Iterates through each row to check for missing data.
3° For each record with missing data, generates a line detailing the missing information.
4°Saves the report to a text file named dados_faltantes.txt.

Note:
The script assumes that missing data is represented by empty cells or NaN values.
The generated text file will be saved in the same directory as the script.

Troubleshooting:
Ensure that the column names in the script match those in your Excel file.
Verify that the path to the Excel file is correct and that the file is accessible.
