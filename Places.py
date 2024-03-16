
class Place:

    def __init__(self, name, set_of_places):
        self.set_of_places = set_of_places
        self.name = name

    def __str__(self):
        return self.name
    
    def lower(self):
        return self.name.lower()
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        print(other.lower() in self.set_of_places, other)
        print(self.set_of_places)
        return other in self.set_of_places
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self.name)
    
