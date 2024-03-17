
class Place:

    def __init__(self, name, aliases):
        self.aliases = aliases
        self.name = name
    
    def __str__(self):
        return self.name
    
    def lower(self):
        return self.name.lower()
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return other.lower() in self.aliases
    
    def __hash__(self):
        return hash(self.name)

def getPlaces():
    norrtalje = Place("norrtälje", {"norrtälje"})
    sodertalje = Place("södertälje", {"södertälje"})
    syd = Place("syd", {"syd", "flemingsberg", "nacka", "flempan", "söderort", "stockholm syd", "västberga"})
    city = Place("city", {"city", "norrmalm", "söder", "kungsholmen", "vasastan", "östermalm", "city", "stockholm city", "stockholm", "söder", "södermalm", "söderort"})
    krim = Place("krim", {"krim", "kvv"})
    misnamed = Place("misnamed", {"misnamed", "felnamn"})
    nord = Place("nord", {"nord", "norrort","norrort", "nord", "solna"})
    return [norrtalje, sodertalje, syd, city, misnamed, krim, nord]
