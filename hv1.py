# noOfCars=0
# noOfCars=0
# total_sum=0
# cars=int(input())
# bikes=int(input())
# amount_cars=cars*40
# amount_bikes=bikes*20
# total_sum=amount_cars+amount_bikes
# print("The total cars parked", cars)
# print("The total bikes parked",bikes)
# print("The amount for cars parked", amount_cars)
# print("The amount for bikes parked", amount_bikes)
# print("The total amount for both cars and bikes is : ",total_sum)
"""another ques """
# apples = int(input("Enter how many apples did the buyer want "))
# if(apples<0):
#     print("Please enter a positive number")
# kiwi = int(input("Enter how many kiwi did the buyer want "))
# grapes = int(input("Enter how many grapes did the buyer want "))

# amountForApples=apples*40
# amountForKiwi=kiwi*50
# amountForGrapes=grapes*60

# totalAmount = amountForApples+amountForKiwi+amountForGrapes
# print("The total amout should be paid by the user is: ", totalAmount)
#hello all

"""loops concepts"""
# pro_1=(int(input("quantity please: ")))
# pro_2=(int(input("quantity please: ")))
# pro_3=(int(input("quantity please: ")))

# l = ['pro_1', 'pro_2', 'pro_3']
# for i in l:
#     print(i)
# if((pro_1<=0) or (pro_2<=0) or (pro_3<=0)):
#     print("please enter positiive value")
# else:
#     print("The amouont you need to pay is : ")
#     total = pro_1*300+pro_2*400+pro_3*500
#     entries={pro_1:300,pro_2:400,pro_3:500}
#     for i,p in entries.items():
#         print(i,p)
#     print('the amount that you need to pay is : ')
#     print(total)





"""List"""
# l = [1,2,3,4,2.5,8.0,'aditya', True]
# print(l)
# print(l[0])
# print(l[6])
# print(l[1:3])
# print(l[::2])
# print(type(l[7]))
# print(l*2)

# l1=['sandeep', 'mohan']
# print(l+l1)

"""Tuples"""
# t=(1,2,3.5,'aditya',False)
# print(t[1])

"""Dictionaries"""
# dict={'ram':20, 'rahul':30, 'raj': 40}
# dict[3]='test'
# print(dict[3])
# print(dict)




# college{}
name=input("enter name")
rollnum=input(("enter roll no"))
# college[name]=rollnum
# print(college)
college1={name:rollnum}
print(college1)