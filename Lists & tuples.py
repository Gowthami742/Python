
# Lists 
marks1 = 94.5
marks2 = 65.5
marks3 = 55.6
marks4 = 65.4
marks5 = 55.1

marks = [94.5, 65.5, 55.6, 65.4, 55.1]
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
# # To know the length of the List
# print(len(marks))

# We can change the value of the Index where as in strings we cannot
student = ["Anil", 17, 95, "Delhi"] 
print(student)
print(student[0])
student[0] = "Sunil" 
print(student)

marks = [87 ,64, 33, 95 , 76]
print (marks[1:4])
print (marks[:4]) 
print (marks[2:])
print(marks[1:]) 
print(marks[-3 : -1])

# List Methods

list = [2 ,1, 3]
list.append(4)
print(list)

list = ['a' , 'b' , 'e', 'd', 'f','g']
list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list = [2 ,1, 3]
list.insert(1,4)
print(list)

list.remove(1)
print(list)

list.pop(list[0])
list.pop()
print(list)


#Tuples

tup = (2 , 3, 4 , 5, 6)
print(tup)
print(type(tup))

tup[0]
print(tup[0])
print(tup[1])

#for single valued tuple we use tup = (1,)
tup = (1,)

#Slicing

tup = (1 , 2 , 3, 4)
print(tup[2:3])

print(tup[:4])


#Tuple Methods 

tup.index(1)
print(tup)

tup.count(3)x   
print(tup)

