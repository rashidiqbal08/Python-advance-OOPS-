##INHERITANCE

#single level inheritance
# class A:                 #superclass
#     def items1(self):
#         print("I have cars")
    
# class B(A):              #sub class
#     def items2(self):
#         print("I have bike")

# father=A()
# child=B()

# child.items1()      #object of class B can access both features from A & B
# father.items1()    #but Class A only can accesse only A

#multi level 

# class A:                 #superclass
#     def items1(self):
#         print("I have cars")
    
# class B(A):              #sub class
#     def items2(self):
#         print("I have bike")
# class C(B):
#     def items3():
#         print("I have cycle")

# father=A()
# child=B()
# grand=C()

#grand can access data frm both A and B
# grand.items2()
# grand.items1() 


#Multiple inheritance

class A:                 #superclass
    def items1(self):
        print("I have cars")
    


class B:              #sub class
    def items2(self):
        print("I have bike")
class C(A,B):                #inherit the feature of both class A and B
    def items3():
        print("I have cycle")

father=A()
child=B()
grand=C()
 

# grand.items2()



