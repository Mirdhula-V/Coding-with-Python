n = int(input())

for i in range(n):
    space = " " * i 
    print(space + ("* " * (n - i)))
for i in range(2,n+1):
    space = " " * (n - i)
    print(space + ("* " * i))