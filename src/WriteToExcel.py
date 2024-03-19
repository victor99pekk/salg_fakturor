from openpyxl import Workbook
import os
import xlwt
from Constants import path, file_format

def getPath(fileName):
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    format = '.xls'
    file = desktop + path + fileName + format
    os.makedirs(os.path.dirname(file), exist_ok=True)
    return file

def write(fileName, df):
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    file = desktop + path + fileName + file_format
    os.makedirs(os.path.dirname(file), exist_ok=True)

    if not os.path.exists(file):
        create_xls_file(file)

    # Create a new workbook and sheet
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Sheet2')

    # Write column names to the first row
    for j, col_name in enumerate(df.columns):
        sheet.write(0, j, col_name)

    # Write the DataFrame data
    for i, row in enumerate(df.values):
        for j, value in enumerate(row):
            sheet.write(i+1, j, value)  # Start writing data from the second row

    # Save the workbook to the file
    workbook.save(file)

def create_xls_file(file_path):
    # Create an empty file
    open(file_path, 'w').close()

def delete_contents(file):
    wb = Workbook()
    ws = wb.active
    ws = wb.create_sheet("Sheet1")    
    ws.delete_rows(1, ws.max_row)
    ws.delete_cols(1, ws.max_column)
    
    # Save the changes to the file
    wb.save(file)
