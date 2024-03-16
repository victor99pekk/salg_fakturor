import pandas as pd
from openpyxl import Workbook


def write(fileName, df):
    path = '/Users/victorpekkari/Documents/salg/outputFiles/'
    format = '.xls'
    file = path + fileName + format
    with pd.ExcelWriter(file, mode='a', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1', startrow=0, header=False)

def delete_contents(file):
    wb = Workbook()
    ws = wb.active
    ws = wb.create_sheet("Sheet1")    
    ws.delete_rows(1, ws.max_row)
    ws.delete_cols(1, ws.max_column)
    
    # Save the changes to the file
    wb.save(file)
