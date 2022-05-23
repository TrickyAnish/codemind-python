n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
for i in l:
    k=0
    for j in i:
        if j.isdigit():
            k=1
    if k==0:
        print("No")
    else:
        print("Yes")