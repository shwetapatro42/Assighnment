{"Telangana": "Hyderabad", "Andhra Pradesh": "Amaravathi", "Tamilnadu": "Chennai", "Rajasthan": "Jaipur", "Delhi": "New Delhi", "Maharastra": "Mumbai", "Karnataka": "Bangalore"}      

import json
Indian_States = {
        "Telangana":"Hyderabad",
        "Andhra Pradesh":"Amaravathi",
        "Tamilnadu":"Chennai",
        "Rajasthan":"Jaipur",
        "Delhi":"New Delhi",
        "Maharastra":"Mumbai",
        "Karnataka":"Bangalore"}

#with open("Indian_States.json","w") as outfile:
#json.dump(Indian_States,outfile, indent=1)
#print("JSON got Appended :\n",Indian_States)
                  ##OR##
data= json.dumps(Indian_States)
file = open('indian_States.json','w')
file.write(data)
file.close()