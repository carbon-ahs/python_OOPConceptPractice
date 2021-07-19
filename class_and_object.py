class Computer:
    def __init__ (self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def config (self):
        print(f'This computer\'s\nCPU: {self.cpu}\nRAM: {self.ram} GB')

comp1 = Computer('i5', 8)
comp2 = Computer('i3', 4)

comp1.config()
comp2.config()