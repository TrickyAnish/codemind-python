s=input()
add=0
for i in s:
    if i.isdigit():
        add=add+int(i)
print(add)