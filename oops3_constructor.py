##CLASS METHODS(constructor)


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
        cls.origin_of_country=new



    

Tata=cars("Harrier","Black",1400000)
Maruti=cars("Swift desire","White",800000)
Tata.display()
Maruti.display()


Tata.change('china')
print(Tata.origin_of_country)  #for tata origin of countt. is changed
print(Maruti.origin_of_country)  #but not for maruti

Maruti.change('USA')
print(Maruti.origin_of_country)  #changed for Maruti
print(Tata.origin_of_country)   #but for tata it remains china
#what is we want to change class variables


#change like this
cars.change('Japan')
print(Tata.origin_of_country)
print(Maruti.origin_of_country)