from Place import Place

norrtalje = Place("norrtälje", {"norrtälje"})
sodertalje = Place("södertälje", {"södertälje"})
syd = Place("syd", {"syd", "flemingsberg", "nacka", "flempan", "söderort", "stockholm syd", "västberga"})
city = Place("city", {"city", "norrmalm", "söder", "kungsholmen", "vasastan", "östermalm", "city", "stockholm city", "stockholm", "söder", "södermalm", "söderort"})
krim = Place("krim", {"krim", "kvv"})
misnamed = Place("misnamed", {"misnamed", "felnamn"})
nord = Place("nord", {"nord", "norrort","norrort", "nord", "solna"})
places = [norrtalje, sodertalje, syd, city, misnamed, krim, nord]

# -------------------


columns_to_keep = ['Datum','Tid', 'Tjänst', 'Distrikt', 'Pers.nr.', 'Resor (km)', 'Resor (kostnad)', 'Kostnad']

# -------------------

required_columns = ['Datum','Tid','Distrikt','Tjänst','Pers.nr.','K-nummer',
                    'Kostnad','Moms','Momsbelopp','Resor (km)','Resor (kostnad)',
                    'Moms (resa)', 'None']

# -------------------

path = '/salg_fakturor/'

# -------------------

file_format = '.xls'

# -------------------

path_to_salg = '/Users/victorpekkari/Documents/salg'

# -------------------

input_start_row = 9

# -------------------

start = 3

# -------------------

taskMapping = {}
taskMapping['blodprov'] = 'Blod'
taskMapping['blod'] = 'Blod'
taskMapping['medicinsk undersökning'] = 'Arrestvård'
taskMapping['arrestvård'] = 'Arrestvård'
taskMapping['död'] = 'Död'
taskMapping['dödsfall'] = 'Död'
taskMapping['rape-kit'] = 'Rape kit'
taskMapping['rape kit'] = 'Rape kit'
taskMapping['Rape kit'] = 'Rape kit'
taskMapping['rättintyg'] = 'kroppsbesiktning+rättsintyg'
taskMapping['kroppsbesiktning+rättsintyg'] = 'kroppsbesiktning+rättsintyg'
taskMapping['kroppsbesiktning'] = 'kroppsbesiktning+rättsintyg'

# -------------------

# Example using manual declaration
price_place_task = {
    'city': {'Blod': 3900, 'Arrestvård': 900, 'Död': 7000, 'Rape kit': 5200, 'Urinprov':1200, 'Utryckning utan uppdrag':1200, 'kroppsbesiktning+rättsintyg':'?'},
    'nord': {'Blod': 1800, 'Arrestvård': 2300, 'Död': 7000, 'Rape kit': 7200, 'Urinprov':1200, 'Utryckning utan uppdrag':1200, 'kroppsbesiktning+rättsintyg':'?'},
    'syd': {'Blod': 2200, 'Arrestvård': 2200, 'Död': 7000, 'Rape kit': 5000, 'Urinprov':1200, 'Utryckning utan uppdrag':1200, 'kroppsbesiktning+rättsintyg':'?'},
    'sodertälje': {'Blod': 3000, 'Arrestvård': 3120, 'Död': 3240, 'Rape kit': 7200, 'Urinprov':1200, 'Utryckning utan uppdrag':1200, 'kroppsbesiktning+rättsintyg':'?'},
    'norrtälje':{'Blod': 3000, 'Arrestvård': 3120, 'Död': 3240, 'Rape kit': 7200, 'Urinprov':1200, 'Utryckning utan uppdrag':1200, 'kroppsbesiktning+rättsintyg':'?'},
}

placeMapping = {
    'solna': 'nord',
    'city': 'city',
    'nord': 'nord',
    'syd': 'syd',
    'södertalje': 'södertalje',
    'norrtalje': 'norrtalje',
    'krim': 'krim',
    'sollentuna': 'nord',
    'västberga': 'syd',
    'flemingsberg': 'syd',
    'nacka': 'syd',
    'norrmalm': 'city',
    'södermalm': 'city',
    'östermalm': 'city',
    'norrtälje': 'norrtälje',
}
