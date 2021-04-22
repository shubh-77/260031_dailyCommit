# Write a Python program to convert a list of tuples into a dictionary

# Python code to convert into dictionary 
def listToDict(old_dict, new_dict): 
   new_dict = dict(old_dict) 
   return new_dict 

# Driver Code  
old_dict = [("Advait", 16), ("Aadar", 5), ("Baba", 37), ("Meena", 7), ("Sanj", 25), ("Sakya", 30)] 
new_dict = {} 
print ("The Dictionary Is ::>",listToDict(old_dict, new_dict)) 
