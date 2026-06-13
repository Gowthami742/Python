#Dictionary
#Eg 1
info =  {
    "key":"value",
    "name":"Gowthami",
    "age":37,
    "Place":"Banglore",
    "is_adult":False
}

print(info)
info["name"]="GowthamiAnanth" #We can add new Key values in Dictionary
info["surname"]="Ananth"
print(info)

#Eg 2
course ={
    "collge":"apnacollge",
    "subjects":["Python","DSA","AI","ML"],
    "Topics":("Dict","set")
}
print(course)

 #We can create empty dictionary also & we can also add values to nulldict


null_dict = {}
null_dict["name"] = "Ashwini"
print(null_dict)


#Nested dictionary

student={
    "name" : "Gowthami",
    "subjects":{
        "chem":98,
        "phy":96,
        "math":85

    }
}
print(student)
print(student["subjects"]) #We can print subjects also

#Dictionary Methods

print(student.keys()) #Returns all the keys ins tudent
print(list(student.keys())) 
print(len(list(student.keys())))

print(len(student)) 

print(student.values()) # Returns all the values in student
print(list(student.values()))
print(student.items()) #Returns all the (Key:Value) pairs in student dict

pairs = list(student.items())
print(pairs[0])

student.update({"City":"Delhi","age": 28})
print(student) # Or same as new_dict

new_dict = {"City":"Delhi","age": 28}
student.update(new_dict)