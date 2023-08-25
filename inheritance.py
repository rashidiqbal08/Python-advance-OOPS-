#
# #CODE FOR AGGREGATION(had a relationship)
# class customer:
#     def __init__(self,name,gender,address):
#         self.name=name
#         self.gender=gender
#         self.address=address
#         self.display()
#     def display(self):
#         print(self.name + self.gender)
#         print(self.address.street,self.address._Address__city,self.address.state)
#
# class Address:
#     def __init__(self,street,city,state):
#         self.street=street
#         self.__city=city
#         self.state=state
#
# ob1=Address('ayodhya bypass','Bhopal','MP')
# ob2=customer('Rashid Iqbal','Male',ob1)
# # ob2.display()


##INHERITANCE
# #simple program for inheritance
# class parent:
#     def __init__(self):
#         self.home='2bhk'
#         self.car='Nexon'
#
#     def food(self):
#         print('I can take the food from my parents')
#
# class child(parent):
#     def mine(self):
#         print("I don't have any thing")
#
# c=child()
# p=parent()
# print(c.car)

# #CONSTRUCTOR IN INHERITANCE:
# class parent:
#     # def __init__(self):
#     #     self.home='2bhk'
#     #     self.car='Nexon'
#     #     print("Inside parent constructor")
#
#     def food(self):
#         print('I can take the food from my parents')
#
# class child(parent):
#     def __init__(self):
#         print("You are inside child class")
#
#     def mine(self):
#         print("I don't have any thing")
#
# c=child()
# # p=parent()
# # print(c)
# # c.

# #use of super keyword
#
# class parent:
#     def car(self):
#         print("Kia 2270")
# class child(parent):
#     def car(self):
#         print("Tata nexon")
#         super().car()
# c=child()
# # p=parent()
# c.car()   #what  id child want to access the parent method of car
# # print(p.car())

# a=list(map(int,input().split()))
# i=0
# for i in a:
#     for j in range(len(a)):
#         if i==a[j+1]:
#             print("YES")
#         else:
#             print("No")

# a=str(2435)
# print(max(a))



##infyTQ
# first_input=input()
# key_val_list=[]
# name_list=[]
# num_list=[]
# temp_list=[]
# final_list=[]
# key_val_list=first_input.split(',')
# for i in key_val_list:
#     temp_list=i.split(':')
#     name_list=temp_list[0]
#     num_list=temp_list[1]
#     name_len=len(name_list)
#
#     maxx=0
#     for j in num_list:
#         if (int(j)<=name_len):
#             if int(j)>maxx:
#                 maxx=int(j)
#     if maxx==0:
#         final_list+='x'
#     else:
#         final_list+=name_list[maxx-1]
# print(final_list)
# print(time.time())


##hexaware question 1 (no of words without vowels)
# a="sky ggh the limit for yy man"
# l=[]
# l=a.split(' ')
# print(l)
# count=0
# vowel='aeiouAEIOU'
# for i in l:
#     print(i)
#     for j in vowel:
#         if j in i:
#             print('alpha')
#             count+=1
# # print(len(l)-count)
# print(len(l)-count)
#
#
# # print(key_val_list)
#

##hexaware(alternative prime sequence , find the less panalities  by adjusting non prime besides prime)
# arr=[1,2,3,5,6,10,12,14,18]
# prime=[]
# non_prime=[]
# count=0
# for i in arr:
#     for j in range(2,i):
#         if i%j==0:
#             count=count+1
#             break
#     if count==0:
#         prime.append(i)
#     else:
#         non_prime.append(i)
#
# for i in prime:
#     if i==1:
#         prime.remove(i)
#         non_prime.append(i)
# print(prime)
# print(non_prime)
# non_prime.sort()
# ans=0
# for i in range(0,((len(non_prime)-len(prime))-1)):
#     ans+=non_prime[i]
# print(ans)
#


##question 2 (if anagram of this string is palindrome or not)
# ##check the no of occurance of letter should be even and only one odd(if)
# s="cdcdcdcdeeeef"
# print(len(s))
# def check(s):
#     count = 0
#     # li=[]
#     for i in s:
#         for j in range(1,len(s)):
#             if i==s[j]:
#                 count=count+1
#             else:
#                 pass
#     print(count)

    # for i in range(0,len(s)-1):
    #     if s[i]==s[i+1]:
    #         count+=1
    #     else:
    #         pass
    # if count>=1:
    #     return 1
    # else:
    #     return 0

# check(s)

n=int(input("No of element: "))
a=list(map(int,input("Element of array: ").split()))
# print(a)
a.sort()

print(a[n-1]+a[n-2])