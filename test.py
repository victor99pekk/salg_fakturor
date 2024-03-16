import pandas as pd
from Places import Place
from Task import Task
from WriteToExcel import write

def getColumnIndex(df, list_of_names):
    for names in list_of_names:
        list = df.index[df.iloc[:, 0] == names].tolist()
        if len(list) > 0:
            return list[0] + 1
    return -1



def getDataFrames(path):
    df = pd.read_excel(path)

    start = getColumnIndex(df, ["Datum"])
    krimvard = getColumnIndex(df, ["Kriminalvården", "KVV", "kvv", "kriminalvården"])

    # Create a new DataFrame without the first n rows
    data = df.iloc[start:].copy()
    data.rename(columns=df.iloc[start-1], inplace=True)

    # for n in range(len(data)-2):
    #     if n < len(data) and pd.isna(data.iloc[n, 0]):
    #         data.drop(index=n, inplace=True)  # Remove row n if column 0 contains NaN
    data.dropna(subset=[data.columns[1]], inplace=True)

    krim = df.iloc[krimvard:].copy()
    krim.rename(columns=df.iloc[start-1], inplace=True)
    krim.dropna(subset=[krim.columns[1]], inplace=True)

    return data, krim

def mapOfDataFrames(df, krim, places, district_col):
    map = {}
    
    for place in places:
        map[place] = []
    return fillMap(map, df, krim, district_col)

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
def fillMap(map, df, krim, district_col):
    for i in range(df.shape[0]):    #iterate map with regular places
        
        row = copySpecificCols(data, i)
        for place in map:
            site = str(row.loc['Distrikt']).lower()

            if site in place.aliases and not row.empty:
                if validTask(str(row.loc['Tjänst'])):
                    map[place].append(row)
                else:
                    map[Place("misnamed", {"misnamed", "felnamn"})].append(row)
                break
    for i in range(krim.shape[0]):  #iterate map with krimvården
        row = copySpecificCols(krim, i)
        if not row.empty:
            if validTask(str(row.loc['Tjänst'])):
                map[Place("krim", ["kvv", "krim"])].append(row)
            else:
                map[Place("misnamed", {"misnamed", "felnamn"})].append(row)

    return map

def createPlaces():  #manually create the places
    norrtalje = Place("norrtälje", {"norrtälje"})
    sodertalje = Place("södertälje", {"södertälje"})
    syd = Place("syd", {"syd", "flemingsberg", "nacka", "flempan", "söderort", "stockholm syd", "västberga"})
    city = Place("city", {"city", "norrmalm", "söder", "kungsholmen", "vasastan", "östermalm", "city", "stockholm city", "stockholm", "söder", "södermalm", "söderort"})
    krim = Place("krim", {"krim", "kvv"})
    misnamed = Place("misnamed", {"misnamed", "felnamn"})
    return [norrtalje, sodertalje, syd, city, misnamed, krim]


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



path = "/Users/victorpekkari/Documents/salg/data/data2.xls"

data, krim = getDataFrames(path)

district_col = district_col(data)

columns_to_keep = ['Datum', 'Tjänst', 'Distrikt', 'Resor (km)', 'Resor (km)', 'Resor (kostnad)', 'Kostnad']


map = mapOfDataFrames(data, krim, createPlaces(), district_col)

for place in map:
    write(str(place), pd.DataFrame(map[place]))

list = getDistrictData("flempan", map)
print(list)

#print(list)


