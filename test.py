import pandas as pd
from Places import Place

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
        #map[place] = [pd.DataFrame(columns=df.columns)]
        map[place] = []
    return fillMap(map, df, krim, district_col)

def validTask(task):
    if any(char.isdigit() for char in task):
        return False
    

def fillMap(map, df, krim, district_col):
    for i in range(df.shape[0]):    #iterate map with regular places
        object = df.iloc[i, district_col].lower()
        for place in map:
            if object in place.aliases and not df.iloc[i, :].empty:
                if validTask(df.iloc[i,'Tjänst']):
                    map[place].append(df.iloc[i, :])
                else:
                    map[Place("misnamed", {"misnamed", "felnamn"})].append(df.iloc[i, :])
                break
    for i in range(krim.shape[0]):  #iterate map with krimvården
        if  not krim.iloc[i, :].empty:
            #print(krim.iloc[i, :])
            map[Place("krim", ["kvv", "krim"])].append(krim.iloc[i, :])

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


map = mapOfDataFrames(data, krim, createPlaces(), district_col)

list = getDistrictData("västberga", map)
print(list)

#print(list)


