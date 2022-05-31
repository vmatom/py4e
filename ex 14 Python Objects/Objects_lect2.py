a = list()
b = str()
c = dict()
d = tuple()
print(dir(a), "\n", dir(b), "\n", dir(c), "\n", dir(d))


class PartyAnimal:  # class is the type of objective
    x = 0  # parameters
    name = ''  # parameters

    def __init__(self):  # constructor is a special block of statements called when an object is created
        print('I am constructed', self.x)

    def party(self):
        self.x = self.x + 1
        print('So far',self.x)
    def __del__(self):
        print("I am destructed", self.x)
an = PartyAnimal()
an.party()
an.party()
an = 42
print ("an contains ", an)
