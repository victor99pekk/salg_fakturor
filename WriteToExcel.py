import pandas as pd
from openpyxl import Workbook
import os
import xlsxwriter as xls

def write2(fileName, df):
    path = getPath(fileName)
    wb = xls.Workbook(path)
    ws = wb.add_worksheet("Sheet1")
    ws.write(0, 0, "#")
    ws.write(0, 1, "Datum")
    ws.write(0, 2, "Tid")
    ws.write(0, 3, "Distrikt")
    ws.write(0, 4, "Tjänst")
    ws.write(0, 5, "Kostnad")
    ws.write(0, 6, "Resor (km)")
    ws.write(0, 7, "Övrigt")

    for index, entry in enumerate(df):
        ws.write(index+1, 0, df[0])
        ws.write(index+1, 1, df[1])
        ws.write(index+1, 2, df[2])
        ws.write(index+1, 3, df[3])
        ws.write(index+1, 4, df[4])
        ws.write(index+1, 5, df[5])
        ws.write(index+1, 6, df[6])
        ws.write(index+1, 7, "")

def getPath(fileName):
    path = '/Users/victorpekkari/Documents/salg/outputFiles/'
    #path = '/outputFiles/'
    format = '.xls'
    file = path + fileName + format
    print(file)
    os.makedirs(os.path.dirname(file), exist_ok=True)
    return file


def write(fileName, df):
    path = '/Users/victorpekkari/Documents/salg/outputFiles/'
    #path = '/outputFiles/'
    format = '.xls'
    file = path + fileName + format
    print(file)
    os.makedirs(os.path.dirname(file), exist_ok=True)

    """ if not os.path.exists(file):  # Check if file exists
        with open(file, "x"):
            pass """
    if not os.path.exists(file):
        create_xls_file(file)

    with pd.ExcelWriter(file, mode='a', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1', startrow=0, header=False)

def create_xls_file(file_path):
    # Open the file in write mode
    with open(file_path, 'x'):
        # Write some data to the file
        pass

def delete_contents(file):
    wb = Workbook()
    ws = wb.active
    ws = wb.create_sheet("Sheet1")    
    ws.delete_rows(1, ws.max_row)
    ws.delete_cols(1, ws.max_column)
    
    # Save the changes to the file
    wb.save(file)
