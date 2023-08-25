##STATIC METHOD
#use of static method(suppose we want to print some statement for some objects of class, so that time static method is used)

class cars:
    def __init__(self,a,b,c):
        self.model=a
        self.color=b
        self.price=c
    
    def display(self):
        print(f"This is Tata {self.model} {self.color} model price is {self.price}")

    @staticmethod
    def statement(string): #this can only be used for induvidual objects
        print(f"This statement is only for {string}")




Tata=cars('Harrier','Black',1600000)
Tata.display()

Tata.statement("Harrier")