import pandas as pd
from Places import Place

def getDataFrames(path):
    df = pd.read_excel(path)

    start = df.index[df.iloc[:, 0] == 'Datum'].tolist()[0] + 1
    krimvard = df.index[df.iloc[:, 0] == 'KVV'].tolist()[0] + 1

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

def fillMap(map, df, krim, district_col):
    for i in range(df.shape[0]):    #iterate map with regular places
        for place in map:
            if df.iloc[i, district_col] == place and not df.iloc[i, :].empty:
                print(df.iloc[i, :])
                map[place].append(df.iloc[i, :])
    for i in range(krim.shape[0]):  #iterate map with krimvården
        if  not krim.iloc[i, :].empty:
            map[Place("krim", ["kvv", "krim"])].append(krim.iloc[i, :])

    return map

def createPlaces():  #manually create the places
    norrtalje = Place("norrtälje", ["norrtälje"])
    sodertalje = Place("södertälje", ["södertälje"])
    syd = Place("Syd", ["syd", "flemingsberg", "nacka", "flempan", "söderort", "stockholm syd", "västberga"])
    city = Place("city", ["city"])
    krim = Place("krim", ["krim", "kvv"])
    misnamed = Place("misnamed", ["misnamed", "felnamn"])
    return [norrtalje, sodertalje, syd, city, misnamed, krim]


def district_col(data):
    if ('Distrikt' or 'distrikt') in data.columns:
        district_column_index = data.columns.get_loc('Distrikt')
    else:
        district_column_index = 2
    return district_column_index

def getDistrictData(name, map):
    for place in map:
        if place == name:
            return map[place]


path = "/Users/victorpekkari/Documents/salg/data/data1.xls"

data, krim = getDataFrames(path)

district_col = district_col(data)


map = mapOfDataFrames(data, krim, createPlaces(), district_col)

list = getDistrictData("kvv", map)
#print(list)
print(list)


