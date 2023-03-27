Assignment 6 Questions 1 part👉 1. 

Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.

import json
file = open("C:\\Users\\Admin\\Desktop\\data science\\Assignment_6\\employee.json",'r')
data = file.read()
file.close()
user = json.loads(data)
print(user)

[
{
    "name":"akash",
    "dob":"18/6/80",
    "height": "5ft",
    "city" : "surat",
    "state":"gujarat"
},
{"name":"Ramesh",
"dob":"25/11/2002",
"height": "5ft",
"city" : "Patna",
"state":"Bihar"},

{"name":"Neha",
"dob":"17/3/99",
"height": "4ft",
"city" : "Mumbai",
"state":"Maharashtra"},

{"name":"Saloni",
    "dob":"25/4/84",
    "height": "5ft",
    "city" : "puna",
    "state":"maharshtra"},

{"name":"Nidhi",
"dob":"24/4/93",
"height": "5ft",
"city" : "raipur",
"state":"chattisgarh"}]
