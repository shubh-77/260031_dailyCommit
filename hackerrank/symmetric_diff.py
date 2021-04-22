# Enter your code here. Read input from STDIN. Print output to STDOUT
#input
M=int(input())
set1=input()
N=int(input())
set2=input()

#spitting and mapping(string to int_list)
x=list(map(int,set1.split()))
y=list(map(int,set2.split()))

#set creation
a=set(x)
b=set(y)

#symmetric difference in each sets
c=a.difference(b)
d=b.difference(a)

#union of difference
e=c.union(d)

#converting set to a list
result=list(e)

#sort the list
result.sort()


for i in range(len(result)):
    print(result[i])