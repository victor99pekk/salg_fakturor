
class Place:

    def __init__(self, name, list_of_places):
        self.list_of_places = list_of_places
        self.name = name

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return other in self.list_of_places
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self.name)
    
