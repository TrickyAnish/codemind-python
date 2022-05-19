n=int(input())
a=0
b=1
c=0
while(c<n):
    a=b
    b=c
    c=a+b
if abs(b-n)>abs(c-n):
    print(c)
elif abs(b-n)==abs(c-n):
    print(b,c)
else:
    print(b)