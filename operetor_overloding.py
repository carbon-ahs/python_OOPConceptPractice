class Student:
    def __init__(self, name, m1, m2):
        self.name = name
        self.m1 = m1
        self.m2 = m2
    
    def __str__(self):
        return self.name

    def __gt__(self, other_std):
        if (self.m1+self.m2) > (other_std.m1+other_std.m2):
            return True
        else:
            return False    

std1 = Student('Shehanuk', 33, 50)
std2 = Student('kasem', 80, 95)

print(std1)

if std1 > std2:
    print(std1)
else:
    print(std2)
