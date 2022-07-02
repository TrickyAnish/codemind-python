n=input()
s=('')
c=0
for i in n:
    if i not in s:
        s+=i
    else:
        c+=1
if c>0:
    print("Not Unique Number")
else:
    print("Unique Number")