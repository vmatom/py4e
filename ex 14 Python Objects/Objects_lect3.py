a = list()
b = str()
c = dict()
d = tuple()
print(dir(a), "\n", dir(b), "\n", dir(c), "\n", dir(d))


class PartyAnimal:  # class is the type of objective
    x = 0  # parameters
    name = ''  # parameters

    def __init__(self, nam):  # constructor is a special block of statements called when an object is created
        self.name = nam
        print('I am constructed', self.name)

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count ", self.x)
s = PartyAnimal("Sally")
s.party()

#an.party()
#an.party()

#print ("an contains ", an)
class Footballfan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points +7
        self.party()
        print(self.name,"points", self.points)

j = Footballfan("Jim")
j.party()
print("BLOB")
j.touchdown()
# inheritance - the ability to extend a class to make a new class
