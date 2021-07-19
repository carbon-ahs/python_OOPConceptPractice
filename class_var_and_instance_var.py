class AnyClass:
    class_var = 100
    def __init__(self):
        self.instance_var1 = 10
        self.instance_var2 = 20

a = AnyClass()
b = AnyClass()
print(f'a.class_var = {a.class_var} b.class.var = {a.class_var}')
AnyClass.class_var = 500
print(f'a.class_var = {a.class_var} b.class.var = {a.class_var}')

b.class_var = 5000 #not worked
print(f'a.class_var = {a.class_var} b.class.var = {a.class_var}')
a.class_var = 50000 #worked !!! how!!!!
print(f'a.class_var = {a.class_var} b.class.var = {a.class_var}')

c = AnyClass()
c.class_var = 500000 #not worked
print(f'a.class_var = {a.class_var} b.class.var = {a.class_var}')

