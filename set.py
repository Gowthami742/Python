#set

collection = {1,2,2,3,4,"hello","world","hello","a"}
print(collection)
print(len(collection)) # total number of items in a set after ignoring duplicate items 
print(type(collection))

nums = {1,2,3,4}
print(nums)

set2 ={1,2,2,2}
print(set2)

#To create empty set 
null_set = set()
print(null_set)

#Set methods add, remove, clear, pop,union, intersection
collect = set()
collect.add(1)
collect.add(2)
collect.add(2)
print(collect)

collect.remove(2)
print(collect)

collect.clear()
print(collect)

course = {"python","DSA","AI","ML"}
print(course.pop()) # Pops any item randomly from course 


set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) # {1,2,3,4,5}

print(set1)
print(set2)

print(set1.intersection(set2))

#Sets 

'''collection = {1,2,3,"Ashwini"}
print(collection)
print(type(collection))
print(len(collection))'''

'''colln={1,1.0,"True"}
print(colln)
print(len(colln))'''

#Creating empty set
'''null_set = set ()
null_set = {1,2,5,6,8,8,9,9}
print(null_set)'''

#Set Methods add,remove,clear,pop,union,intersection

'''collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apnacollege") #We can add string
collection.add((2,5,6)) #We can add tuples
print(len(collection))'''
'''collection.add([2,5,6])  #We cannot add Lists , TypeError: unhashable type: 'list'''


collection={"Hello","Apnacollege","Hello"}
print(collection.pop())


'''collection.remove(7) #Key error ,because the Key 7 is not present 
print(collection)
'''

set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))

print(set1.intersection(set2))


# #Examples

# dictionary = {
#     "cat" : "a small animal",
#     "table": ["a piece of furniture","list of facts and figures"]
# }

# print(dictionary)


# subjects = {
#     "python","java","c++","python","javascript","python","java",
#     "python","java","c++","c"
# }
# print(subjects)
# print(len(subjects))


# # marks = {}

# # x= int(input("enter chem marks: "))
# # marks.update({"phy" : x})

# # y = int(input("enter phy marks: "))
# # marks.update({"chem" : y})

# # z = int(input("enter math marks: "))
# # marks.update({"math" : z})



# # values = {9,"9.0"}
# # print(values)

# # values = {
# #     ("float",9.0),
# #     ("int",9)
# # }
# # print(values)


# '''i=0
# while i <=5:
#     print("i",i)
#     i+=1
# '''


# '''fruits = ["apple","orange","mango"]
# for fruit in fruits:
#     print(fruits)'''

# '''
# text = "python"
# for char in text:
#     print(text)
# '''
# '''total = 0
# for i in range(1,6):
#     total+=1
#     print("sum:",total)'''

# #nested Loop
# '''for i in range(1,4):
#     for j in range (1,5):
#         print("i:",i,"j:",j)'''


# #wap to print numbers from 1 t0 5

# # i=1
# # while i <=5:
# #     i+=1
# #     print("i:",i)
# # print("Loop ended")



# #wap to print numbers from 5 t0 1
# # i = 5
# # while i >= 1:
# #     print(i)
# # i -= 1
# # print("loop ended")


# z=0
# while z<= 100:
#     z+=1
#     print(z)