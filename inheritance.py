class A:
    def funcA():
        print('funcA is working')
class B:
    def funcB():
        print('funcB is working')
class C(A): #Single level inheritance
    def funcC():
        print('funcC is working')
class D(C): #muli level inheritance 
    def funcD():
        print('funcD is working')
class E(A, B): #multiple inheritance
    def funcE():
        print('funcE is working')
