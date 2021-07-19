class Student:
    school_name = 'BAUET'
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def get_m1(self): #accessor
        return self.m1

    def set_m1(self, new_value): #mutator
        self.m1 = new_value


    @classmethod #decorator for class methods
    def get_school_name(cls):
        return cls.school_name
    
    @staticmethod
    def info():
        print('its student class')

student1 = Student(33, 33, 80)
student2 = Student(80, 33, 80)

print(Student.get_school_name())
Student.info()
student1.info()

print(student1.get_m1())
student1.set_m1(500)
print(student1.get_m1())
