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

path = '/salg_fakturor/'

# -------------------

file_format = '.xls'

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

priceMapping = {}