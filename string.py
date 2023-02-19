
# Function to reverse a string
# by converting string to list
# then reversed it and again convert it to string
def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)
 
s = "impressive in appearance"
 
print("The original string  is : ", s)
 
print("The reversed string(using reversed) is : ", reverse(s))