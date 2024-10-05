n = int(input())

for i in range(1,n+1):
    space = " " * (n - i)
    star = "* " * i 
    print(space + star)
for j in range(1,n):
    space = " " * j 
    star = "* " * (n - j)
    print(space + star)