import pickle
class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr


e = Employee(100, 'rajan', 1000, 'hyd')
print(e.eno, e.ename, e.esal, e.eaddr)



