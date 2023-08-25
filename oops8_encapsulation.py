# class bank:
#     def __init__(self):
#         self.pin='1234'
#         self.balance='1000'
#         # self.menu()
#
#
#
# ob=bank()
# print(ob.balance)
class bank:
    def __init__(self):
        self.pin='1234'
        self.__balance='1000'   #making balance variable private

        # self.menu()

    # accessing the balance we programmer have to encapsulate it in getter and setter method.
    def get(self):
        return self.__balance

    def setter(self,balance):
        if type(balance)==int:
            self.__balance=balance

ob=bank()
# print(ob.balance)   #now we wont access
print(ob.get())
ob.setter(2000)    #balance has been changed.
print(ob.get())