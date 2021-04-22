tc = int(input())
i=1
while(i<= tc):
    n1 = int(input())
    set1 = set(map(int, input().split()))
    n2 = int(input())
    set2 = set(map(int, input().split()))
    print(set1.issubset(set2))
    i=i+1