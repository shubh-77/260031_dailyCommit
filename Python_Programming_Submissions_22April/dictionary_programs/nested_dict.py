test_dict = {'Melon' : 4, 'Peach' : 5, 'Chikko' : 9} 
test_list = [8, 3, 2]
  
# printing original dictionary and list
print("The old dictionary is : " + str(test_dict))
print("The old list is : " + str(test_list))
  
# zip() and dictionary comprehension mapped in one liner to solve
res = {idx: {key : test_dict[key]} for idx, key in zip(test_list, test_dict)}
          
# print result 
print("The mapped dictionary : " + str(res))