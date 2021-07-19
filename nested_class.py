class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.club = self.StudentClub()


    def show(self):
        print(self.name, self.roll)
        self.club.show()

    class StudentClub:
        def __init__(self):
            self.club_name = 'Hudai Club'
            self.post = 'hudai'

        def show(self):
            print(self.club_name, self.post)
    

std1 = Student('Shehanuk', 6)
std2 = Student('kasem', 65)

std1.show()
std1.club.show()