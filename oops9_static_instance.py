class bank:
    #static variable
    ifcs=2

    def __init__(self):
        self.ifc=bank.ifcs
        bank.ifcs+=1

        #Instance variable
        self.no=1
        self.no+=1


obj1=bank()
obj2=bank()
print(obj1.ifc)
print(obj2.ifc)

print(obj2.no)
print(obj2.no)


