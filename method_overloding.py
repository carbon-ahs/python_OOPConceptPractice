class Numbers:
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s

numbers = Numbers()

print(numbers.sum(10+20+30))
print(numbers.sum(10+20))
print(numbers.sum(10))
print(numbers.sum())