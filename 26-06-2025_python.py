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


employee2={
    id:2,
    "Name":"Akhil",
    "Email":'Akhil@gmail.com'
}
employees=[]
employees.append(employee)
employees.append(employee2)
print(employees)

# Create individual employee dictionaries
employee1 = {
    "id": 1,
    "Name": "Nikhil",
    "Email": "nikhil@gmail.com"
}
employee1["Gender"] = "Male"
employee1.update({"Country": "India"})

employee2 = {
    "id": 2,
    "Name": "Akhil",
    "Email": "akhil@gmail.com"
}
employee2["Gender"] = "Male"
employee2.update({"Country": "India"})

employee3 = {
    "id": 3,
    "Name": "Sneha",
    "Email": "sneha@gmail.com"
}
employee3["Gender"] = "Female"
employee3.update({"Country": "India"})

employee4 = {
    "id": 4,
    "Name": "Rahul",
    "Email": "rahul@gmail.com"
}
employee4["Gender"] = "Male"
employee4.update({"Country": "India"})

employee5 = {
    "id": 5,
    "Name": "Priya",
    "Email": "priya@gmail.com"
}
employee5["Gender"] = "Female"
employee5.update({"Country": "India"})

employee6 = {
    "id": 6,
    "Name": "Kiran",
    "Email": "kiran@gmail.com"
}
employee6["Gender"] = "Male"
employee6.update({"Country": "India"})

# Create employee list
employees = []
employees.append(employee1)
employees.append(employee2)
employees.append(employee3)
employees.append(employee4)
employees.append(employee5)
employees.append(employee6)

# Use pop to remove a key
employee3.pop("Email")

# Use del to delete a key
del employee4["Country"]

# Add a new key
employee5["Phone"] = "9998887777"

# Update existing value
employee1["Name"] = "Nikhil Reddy"

# Use get to access key safely
print(employee3.get("Email", "Email not found"))

# Print selected values
print(employee1["Name"], employee1["Email"])
print(employee2["Name"], employee2["Email"])
print(employee5["Name"], employee5["Phone"])

# Print full list of employees
print(employees)
