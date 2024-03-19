from openpyxl import Workbook
import os
import xlwt
import xlsxwriter as xlsx
from Constants import path, file_format, start

def getPath(fileName):
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    format = '.xls'
    file = desktop + path + fileName + format
    os.makedirs(os.path.dirname(file), exist_ok=True)
    return file

def write(fileName, df):
    current_row = start
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    file = desktop + path + fileName + file_format
    os.makedirs(os.path.dirname(file), exist_ok=True)

    if not os.path.exists(file):
        create_xls_file(file)

    # Create a new workbook and sheet
    workbook = xlsx.Workbook(file)
    workbook = xlsx.Workbook(file, {'nan_inf_to_errors': True})
    sheet = workbook.add_worksheet('Sheet2')
    yellow_format = workbook.add_format({'bg_color': 'yellow', 'font_size': 14})

    column_width = 20  # 20 characters wide
    sheet.set_column(0, len(df.columns) - 1, column_width)
    header_format = workbook.add_format({'font_size': 20})  # Adjust font size as needed
    sheet.write(0, 0, fileName, header_format)

    # Write column names to the first row
    for j, col_name in enumerate(df.columns):
        sheet.write(1, j, col_name, yellow_format)
        current_row += 1

    # Write the DataFrame data
    for i, row in enumerate(df.values):
        for j, value in enumerate(row):
            sheet.write(i + 2, j, value)  # Start writing data from the third row
            current_row += 1

    # Save the workbook to the file
    workbook.close()


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
