def pa(n):
    n=str(n)
    if(n==n[::-1]):
        return True
    else:
        return False
n=int(input())
a=n+1
b=n-1
while(1):
    if pa(a)==1:
        break
    a+=1
while(1):
    if pa(b)==1:
        break
    b-=1
if abs(a-n)==abs(b-n):
    print(b,a)
elif abs(a-n)>abs(b-n):
    print(b)
else:
    print(a)