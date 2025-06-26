tupleList = (1,2,3)

''' Dictionary items are ordered, Mutual, and not allow duplicates.
syntax: 
Variable_name ={key:value,key:value}
key should be a named string and unique'''

'''ex :-'''

employee={
    id:1,
    "Name":"Nikhil",
    "Email":'Nikhil@gmail.com'
}
'''Add item to dict'''
'''dict [key]=value'''
employee["Gender"]="Male"
print(employee)

'''Update: is used to add item to a dict.'''
employee.update({"country":"India"})
print(employee)

'''get/acces dict values- By using dict key'''
print(employee["Name"])
print(employee["Email"],employee["Gender"])


