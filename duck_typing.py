class Car:
    def go(self):
        print('vuuuu')

class Ambulance:
    def go(self):
        print('pa pu pa pu')
        print('vuuuu')

class BusStand:
    def people_go(self, transport):
        transport.go()

gari1 = Car()
gari2 = Ambulance()

shakhipur = BusStand()

shakhipur.people_go(gari1)
shakhipur.people_go(gari2)