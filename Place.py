
class Place:

    def __init__(self, name, aliases):
        self.aliases = aliases
        self.name = name
        self.norrtalje = Place("norrtälje", {"norrtälje"})
        self.sodertalje = Place("södertälje", {"södertälje"})
        self.syd = Place("syd", {"syd", "flemingsberg", "nacka", "flempan", "söderort", "stockholm syd", "västberga"})
        self.city = Place("city", {"city", "norrmalm", "söder", "kungsholmen", "vasastan", "östermalm", "city", "stockholm city", "stockholm", "söder", "södermalm", "söderort"})
        self.krim = Place("krim", {"krim", "kvv"})
        self.misnamed = Place("misnamed", {"misnamed", "felnamn"})
        self.nord = Place("nord", {"nord", "norrort","norrort", "nord", "solna"})

    @staticmethod
    def getPlaces(self):
        return [self.norrtalje, self.sodertalje, self.syd, self.city, self.misnamed, self.krim, self.nord]
    
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
    
