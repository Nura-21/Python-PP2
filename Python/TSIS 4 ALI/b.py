n = int(input())
l = [int(l) for l in input().split()]
for i in l:
    if i %2==0:
        print(l[i],end=" ")