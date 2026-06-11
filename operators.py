#Operators
#Arithmetic operators
'''
a=10
b=3
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a//b) #floor division
print(a%b) #Remainder
print(a**b) #Modulus '''

'''price =200
gst = 18
total= price + (price*gst/100)
print(total)'''

#Assignment Operators

balance = 5000

'''x=5
x+=3 # x=x+3 i.e 5+3=8
print(x)'''

'''carttotal=1000
carttotal +=500 #added an new item
print(carttotal)'''

'''x=10
x-=4 # x=x-4 i.e 10-4=6
print(x) '''

'''carttotal =5000
carttotal-=1500 #subtract  new item
print(carttotal) '''

'''x=2
x*=5 # x=x*2 i.e 5*2=10
print(x) '''
 
'''carttotal=5000
carttotal*=1500 #Multiply  new item
print(carttotal)'''

"""x=10
x%=3 # x=x/3 i.e 10/3=1
print(x) """

"""x=10
x//=3 # x=x//3 i.e 10/3=3
print(x) """

'''wallet=1000
wallet+=500
wallet-=200
wallet*=2
print("Wallet balance:",wallet) '''

'''=:Store
+=:add
-=:sub
*=:Multiply
/=:Divide
%=:Remainder/Modulus
//=:Floor division
**=: power & store'''


#Comparsion/ Relational Operators

'''savedpassword = "Python1234"
enteredpassword = input("Enter password:")
print(savedpassword == enteredpassword)'''

'''age = 20
print(age>21)'''

'''stock = 5
print(stock<4) '''

'''marks = 35
print(marks >=35)'''

'''marks = int(input("Enter marks:"))
print("pass:",marks>=35)
print("distinction:",marks>=75)'''

#Logical Operators 

#and operator


'''age =18
marks=60
print(age>=18 and marks>=60)'''

#conditions:balance > withdrawal amount, card is active
'''balance = 50000
withdrawalamount = 20000
cardactive = True 
print(balance >= withdrawalamount and cardactive)'''

#or operator

'''email_login=False
phone_login=True
print(email_login or phone_login)'''

'''day="sunday"
print(day=="saturday" or day=="monday")'''

#not operator 

'''a=6
b=5
print(not(a>b))'''

'''is_blocked=True
print(not(is_blocked))
'''

'''age = 24
degree=True
blacklisted=False
eligible=(age>=21 and age<=35) and degree and not blacklisted
print(eligible)'''

#Indentity Operators 
'''x=10
y=10
print(x is y)'''

'''a=10
b=20
print(a is not b)'''
