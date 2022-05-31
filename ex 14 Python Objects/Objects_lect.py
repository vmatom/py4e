
class PartyAnimal:  # class is the type of objective
    x = 0  # parameters
    name = ''  # parameters

    def __init__(self, nam):  # Code of the class
        self.name = nam
        print(self.name,'constructed')

    def party(self):
        self.x += 1
        print(self.name,'party count',self.x)


q = PartyAnimal('Quincy')
q.party()
m = PartyAnimal('Miya')
m.party()
q.party()
# print(dir(PartyAnimal))
