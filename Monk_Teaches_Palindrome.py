t=int(input())
for i in range(t):
    s=input()
    x=s[::-1]
    if s==x:
        print("YES",end=' ')
        if len(s)%2==0:
            print("EVEN")
        else:
            print("ODD")
    else:
      print("NO")