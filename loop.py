#Loops
#while loop

#WAP to print hello 5 times
'''count = 1
while count <=5:
    print("hello:",count)
    count+=1
    print(count)'''

'''i=1
while i <= 5:
    print("apnacollge:",i)
    i+=1
    print(i)'''

#WAP to print helloworld 100 times   
'''j=1
while j<=100:
    print("helloworld:",j)
    j+=1
    print(j) 
'''
#WAP to print numbers from 1 to 5
'''i=1
while i<=5:
    print("i:",i)
    i+=1
    print("Loop ended")
'''
#WAP to print numbers from 5 to 1

'''i=5
while i >=1:
    print("i:",i)
    i-=1

    print("Loop Ended")'''
 
 #WAP to print numbers from 1 to 100

'''i=1
while i<=100: #Stopping condition (which means loop will run till i value will be true )
    print("i:",i)
    i+=1
    print("Loop Ended")'''


 #WAP to print numbers from 100 to 1

# i=100
# while i >=1:
#     print("i:",i)
#     i-=1
#     print("Loop Ended")


#WAP print the multiplication table of number n

# n= int(input("Enter number:"))
# i =1
# while i <=10:
#     print(n*i) #Where we can give the input 
#     i+=1

#Print the elements of the following list using a loop:

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# idx=0
# while idx < len(nums):
#     print(nums[idx]) #num[0],num[1],num[2],..
#     idx+=1


#WAP to print the List of Heroes Names

# heroes = ["ironman","thor","batman","sipderman"]

# i=0
# while i < len(heroes):
#     print(heroes[i])
#     i+=1

# Search for a number x in this tuple using loop:

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# x = 36
# i =0
# while i < len (nums):
#     if(nums[i]==x):
#      print("FOUND at idx",i)
#     else:
#        print("finding..")
#     i+=1


#break

i=1
while i <= 5:
    print(i)
    if (i ==3):
      break
    i+=1
print("End of the loop")


#continue
# i=0
# while i <= 5:
#    if (i ==3):
#       i+=1
#       continue #skip
#    print(i)
#    i+=1

#To print only Odd nunbers from 1 to 10 
i=1
while i <= 10:
   if (i%2 ==0 ):
      i+=1
      continue #skip
   print(i)
   i+=1

# i=1
# while i <= 10:
#    if (i%2 ==0 ):
#       i+=1
#       continue #skip
#    print(i)
#    i+=1

# i=1
# while i <= 10:
#    if (i%2 !=0 ):
#       i+=1
#       continue #skip
#    print(i)
#    i+=1



#for loop 
# Ex 1: list
# nums = [1,2,3,4,5]
# for val in nums:
#    print(val)

# EX 2:
   veggies = ["brinjal","potato","tomato","cucumber"]
   for val in veggies:
      print(val)

#Ex 3:
tup = (2,4,6,8,10)
for val in tup:
   print(val)

#Ex 4:
# str = ("Apnacollege")
# for char in str:
#    print(char)


#    str = ("Apnacollege")
# for char in str:
#    print(char)
# else:
#    print("END")


#Print the elements of the following list using a loop:

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for val in num:
#    print(val)

# Search for a number x in this tuple using loop:

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100,49)

# x = 49
# idx = 0
# for el in nums:
#    if(el == x ):
#       print("Number FOUND at idx",idx)
#       idx+=1


#Range

# seq = range(10)
# for i in seq:
#    print(i)


#    for i in range(10): #range(stop)
#       print(i)

# for i in range(2,10): #range(start,stop)
#       print(i)   


# for i in range(2,10,2): #range(start,stop,step)
#       print(i) 

# for i in range(2,100,2):
#    print(i)

#    for i in range(1,100,2):
#      print(i)


# Print numbers from 1 to 100.

# for i in range(1,101):
#    print(i)



# Print numbers from 100 to 1.

# for i in range(100,1,-1):
#    print(i)

# Print the multiplication table of a number n.using for & range( )
# n= int(input("Enter number:"))
# for i in range(1,10):
#    print(n*i)

#range

# for i in range(5):
#    pass
#    print("some useful work")


# WAP to find the sum of first n natural numbers. (using while)

n=7
sum= 0
for i in range(1,n+1):
   sum += i
   print("total sum=",sum)


# WAP to find the factorial of first n numbers. (using while)
# n = 5
# fact=1
# i=1
# while i <=n:
#    fact*=i
#    i+=1
#    print("factorial=",fact)


   n = 5
   fact = 1
   for i in range (1, n+1):
    fact *= i
    print("factorial =", fact)