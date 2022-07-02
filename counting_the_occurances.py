s=input()
p=input()
c=0
for i in s:
    if i==p:
        c+=1
if c>0:
    print(c)
else:
    print("-1")