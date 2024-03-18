import os
import pandas as pd
from Place import Place
from Task import Task
from WriteToExcel import write


columns_to_keep = ['Datum','Tid', 'Tjänst', 'Distrikt', 'Pers.nr.', 'Resor (km)', 'Resor (km)', 'Resor (kostnad)', 'Kostnad']

def start_row(df, list_of_names):
    for names in list_of_names:
        list = df.index[df.iloc[:, 0] == names].tolist()
        if len(list) > 0:
            return list[0] + 1
    return -1

def getDataFrames(path):
    df = pd.read_excel(path)

    start = start_row(df, ["Datum"])
    krimvard = start_row(df, ["Kriminalvården", "KVV", "kvv", "kriminalvården"])
    # Create a new DataFrame without the first n rows
    data = df.iloc[start:].copy()
    data.rename(columns=df.iloc[start-1], inplace=True)
    data.dropna(subset=[data.columns[1]], inplace=True)

    krim = df.iloc[krimvard:].copy()
    krim.rename(columns=df.iloc[start-1], inplace=True)
    krim.dropna(subset=[krim.columns[1]], inplace=True)


    return data, krim

def validTask(task):
    if any(char.isdigit() for char in task):
        return False
    if task.lower() not in Task.create_validTasks():
        return False
    return True
    
def copySpecificCols(data, i):
    row = data.iloc[i].copy()
    row = row[columns_to_keep] 
    row['Tjänst'] = Task.create_validTasks()[row['Tjänst'].lower()]
    row['Kostnad'] = Task.price(row['Tjänst'], row['Distrikt'])
    return row
    
#8 col
def fillMap(map, df, krim):
    print()
    for i in range(df.shape[0]):    #iterate map with regular places
        row = copySpecificCols(df, i)
        for place in map:
            site = str(row.loc['Distrikt']).lower()

            if site in place.aliases and not row.empty:
                if validTask(str(row.loc['Tjänst'])):
                    map[place].loc[len(map[place].reset_index(drop=True))] = row
                else:
                    p = Place("misnamed", {"misnamed", "felnamn"})
                    map[p].loc[len(map[p])] = row
                print(map)
                break
    print(map)
    for i in range(krim.shape[0]):  #iterate map with krimvården
        row = copySpecificCols(krim, i)
        if not row.empty:
            p = Place("krim", ["kvv", "krim"])
            if validTask(str(row.loc['Tjänst'])):
                map[p].loc[len(map[p])] = row
            else:
                map[Place("misnamed", {"misnamed", "felnamn"})].loc[len(map[Place("misnamed", {"misnamed", "felnamn"})])] = row

    return map

def createPlaces():  #manually create the places
    norrtalje = Place("norrtälje", {"norrtälje"})
    sodertalje = Place("södertälje", {"södertälje"})
    syd = Place("syd", {"syd", "flemingsberg", "nacka", "flempan", "söderort", "stockholm syd", "västberga"})
    city = Place("city", {"city", "norrmalm", "söder", "kungsholmen", "vasastan", "östermalm", "city", "stockholm city", "stockholm", "söder", "södermalm", "söderort"})
    krim = Place("krim", {"krim", "kvv"})
    misnamed = Place("misnamed", {"misnamed", "felnamn"})
    nord = Place("nord", {"nord", "norrort","norrort", "nord", "solna"})
    return [norrtalje, sodertalje, syd, city, misnamed, krim, nord]


def district_col(data):
    if ('Distrikt' or 'distrikt') in data.columns:
        district_column_index = data.columns.get_loc('Distrikt')
    else:
        district_column_index = 2
    return district_column_index

def getDistrictData(name, map):
    for place in map:
        if name in place.aliases:
            return map[place]

def run(path, map):
    #path = "/Users/victorpekkari/Documents/salg/data/test.xlsx"
    data, krim = getDataFrames(path)
    fillMap(map, data, krim)

def sort(inputFolder, outputFolder):
    dataKeeper = dataKeeper()
    for filename in os.listdir(inputFolder):
            file_path = os.path.join(inputFolder, filename)
            # Check if the current item is a file, and Check if the file has a .xls extension using endswith()
            if os.path.isfile(file_path) and filename.endswith('.xls'):
                dataKeeper = run(file_path, dataKeeper)
    for place in Place.getPlaces():
        outputPath = outputFolder + "/" + str(place) + ".xls"
        write(outputPath, dataKeeper.map[place])


#run("/Users/victorpekkari/Documents/salg/data", "/Users/victorpekkari/Documents/salg/output")
