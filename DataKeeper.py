import pandas as pd
from Place import Place, getPlaces

class DataKeeper:

    def __init__(self):
        self.map = {}
        self.targetFolder = ""
        self.inputPath = ""
        self.columns_to_keep = ['Datum', 'Tjänst', 'Distrikt', 'Resor (km)', 'Resor (kostnad)', 'Kostnad']
        self.places = getPlaces()
        for place in self.places:
            map[place] = pd.DataFrame(columns=self.columns_to_keep)