li = [] 
# taking list size
n = int(input("Enter size "))

# appending and sorting
for i in range(1, n+1): 
    ele = int(input("Enter element: ")) 
    li.append(ele) 
li.sort() 

print("The sorted list: ", li) 
print("The second smallest value of this list: ",li[1])