#creating class cars
class Cars:      #cars will take argument only if we have __init__ func
    
    #NOW WE'LL SEE THE USE OF CONSTRUCTOR(It's a method to pass arugment to class(Cars))
    def __init__(self,a,b,c):   #here we'll consider 'self' as an object
        self.model=a    
        self.price=b
        self.color=c
    
    #creating some methods  (to understant the 'self', thats how we can modifiy codes(flexiblity))
    def details(self):
        print(f"this, {self.color} color {self.model} price is {self.price}")

    
 


#creating instance
Tata =Cars('Harrier',1400000,'Black')   #we'll give arguments to the class 
Maruti = Cars("Swift desire",800000,'White')  #we can also pass arugment from here(bcoz we have constructor)

# Tata.printt()
# Maruti.printt()



##baisc war to make object variables

# Tata.model='Harrier'
# Tata.price=1400000
# # Tata.color='Black'
# Maruti.model="swift desire"
# Maruti.price=800000
# Maruti.color='White'



Tata.details()   #variable of Tata will be passed as an argument
Maruti.details()  #variable of Maruti will be passed as an argumment
    
    #(BTW it's increasing the reusability)


# for i,j in Tata.__dict__.items():
    # print(i,j)