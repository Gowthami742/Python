#Data Types 

#int Example 
""" math=22
social=95
total=math+social
print(type(total)) """  # Multi line comment 

#float Example 
price=199.99
temperature=35.4
print(price)

#complex Example 
z=2+3j
print(z)

#string
name="Gowthami"
city="Bangalore"
print(city[1:-1])

username="Gowthami12345"
print(len(username)) # to find the length of username

# list

'''marks = [95 , 80, 70]
print(marks)
marks[0]=100
print(marks) '''

'''fruits = ["Apple", "mango", "orange"]
print(fruits)
fruits[0]="watermelon"
print(fruits) '''

'''numbers=[1,3,2,4,8,7]
numbers.append(5) #adds number atlast
print(numbers)
numbers.remove(3) #removes selected number
print(numbers)
numbers.pop() #removes the last element
print(numbers)
prints(numbers[1:4]) #slicing '''

#tuple

'''numbers=(10,20,30)
print(numbers)
print(numbers[0]) '''


#set datatype
"""numbers={10,20,30,20,40,10}
print(numbers)

rollnumbers={101,201,301}
rollnumbers.add(601)
rollnumbers.remove(201)
print(rollnumbers)"""

#Boolean datatype
'''x=True
print(type(x))

marks=75
print(marks >=35)'''

#None datatype
'''x=None
print(type(x))

current_user=None

a=None
b=None
print(a is b)

a=None
print(a+5)''' # This will gives error (We cannot add Nonetype with integer)


#Checking Datatypes
'''
a=1
print(type(a))

b=2.5
print(type(b))

c=True
print(type(c))

d=None
print(type(d))

e=[10,30,20]
print(type(e))

f=(1,2,4,5)
print(type(f))

g="Gowthami"
print(type(g)) '''

#Type Conversion