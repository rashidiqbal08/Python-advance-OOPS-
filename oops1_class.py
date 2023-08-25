##importance of classes:- class can provide a easy way of keeping
    #  the data members and methods in one place


class Student:
    pass              #class will never be empty

Shrija =Student()   #objects of class student (instances)
Rashid =Student()  

print(Shrija,Rashid)  #these are two diff objects with diff add. location

#adding variable to the objects

Shrija.name="Shrija Jha"
Shrija.course="BioTech"
Shrija.age=21

Rashid.name="Rashid Iqbal"
Rashid.course="BTech"
Rashid.age=21


print(Rashid.name)
print(Shrija.name)


##creating another claass named Employee

class Employee:
    company  ='IBM'     #this variable is common for all the objects of Employee
    pass

Rashid = Employee()
Shrija = Employee()

Rashid.name='Rashid iqbal'
Rashid.job= 'Data scientist'
Rashid.salary= 650000

Shrija.name='Shrija jha'
Shrija.job= 'medecine researcher'
Shrija.salary= 550000

print(Rashid.job,"  ",Shrija.job)

#we can print the object's attribute by using dict func
print(Rashid.__dict__)

#we can access this variable from any objects 
print(Shrija.company)
print(Rashid.company)
print(Employee.company)  #even from class itself

#we canonly update the common variable from Employee only

Employee.company='TCS'  #if we try to change from object then it won't change(it will create a new variable)
print(Rashid.company)
 