from openpyxl import Workbook
import os
import xlsxwriter as xlsx
from Constants import path, file_format, start
import random
from Constants import *
import string


def create_xls_file(file_path):
    # Create an empty file
    open(file_path, 'w').close()

def createTime():
    array = []
    threeNbr = random.random()
    length = 5

    char = random.choice([':', '.'])
    string = ""

    if threeNbr < 0.5:
        length = 4
    for i in range(length):
        nbr = random.randint(0, 9)
        if i != 2:
            string = char[random.randint(0, 1)] + string
        else:
            string = str(nbr) + string
    return string


def createDate():
    return '2403' + str(random.randint(1, 30))

def getDistrict():
    return random.choice(list(placeMapping.keys()))

def getTask():
    return random.choice(list(taskMapping.keys()))

def persNbr():
    string = ""
    length = 4
    nbr = random.randint(0, 2)
    if nbr == 0:
        return 'okänd'
    elif nbr == 1:
        length = 6
    for i in range(length):
        string += str(random.randint(0,9))
    return string

def random_string():
    length = random.randint(1, 12)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random string of specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def cost():
    cost = str(random.randint(1000, 10000))
    randomNbr = random.randint(0, 2)
    if randomNbr == 0:
        return cost
    elif randomNbr == 1:
        return cost + 'kr'
    else:
        return cost + ' kr'

def Moms():

    if random.randint(0,1) == 0:
        return str(random.random())
    if random.randint(0,1) == 0:
        return str(random.random())
    return str(random.random()) + '%'



    


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
    yellow_format = workbook.add_format({'bg_color': 'yellow', 'font_size': 14, 'bold':True})

    column_width = 20  # 20 characters wide
    sheet.set_column(0, len(df.columns) - 1, column_width)
    header_format = workbook.add_format({'font_size': 20})  # Adjust font size as needed
    sheet.write(0, 0, fileName.split("/")[0], header_format)

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
