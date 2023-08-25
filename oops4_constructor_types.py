
##concept of alternative constructor (from line 17)

class cars:
    origin_of_country='India'   #this variable is for both tata and maruti
    def __init__(self,a,b,c):
        self.model=a
        self.color=b
        self.price=c

    def display(self):
        print(f"This is {self.model} {self.color} and price is {self.price}")

    @classmethod
    def change(cls,new):
        origin_of_country=new
        
    @classmethod
    def from_str(cls,string):
        variable=string.split("-")
        print(variable)
        return cls(variable[0],variable[1],variable[2])  
        

    

Tata=cars("Harrier","Black",1400000)
Maruti=cars("Swift desire","White",800000)

#using getattr(,) for accessing through attribute name
print(getattr(Tata,'model'))


Tata.display()
Maruti.display()
# Mahindra.display()

##concept of alternative constructor
    #(What if we want to creat another instance of class cars.)
    #in line 17 we have added another instance but what if we pass all variable as string

Mahindra=cars.from_str("Scarpio-White-1600000")
print(Mahindra.model)