n=int(input())
m=int(input())
s=0
p=0
for i in range(1,n//2+1):
    if n%i==0:
        s=s+i
for j in range(1,m//2+1):
    if m%j==0:
        p=p+j
if s==m and p==n:
    print("Amicable")
else:
    print("Not Amicable")