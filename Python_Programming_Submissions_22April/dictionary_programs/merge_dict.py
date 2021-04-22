# Write a Python script to merge two Python dictionaries
# initializing 2 dictionaries

fruits = {"apple": 1, "orange" : 3, "tangerine": 5}
dry_fruits = {"walnut": 7, "almond": 4, "pistachio": 6}

# updating the fruits dictionary
fruits.update(dry_fruits)
## printing the fruits dictionary
## it contains both the key: value pairs
print(fruits)
# {'pistachio': 6, 'apple': 1, 'orange': 3, 'almond': 4, 'tangerine': 5, 'walnut': 7}