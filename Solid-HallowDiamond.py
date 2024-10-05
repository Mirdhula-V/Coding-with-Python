n = int(input())

for i in range(1,n+1):
    corner_space = " " * (n-i)
    if(i==1):
        print(corner_space + "*")
    else:
        stars = ("* ") * i
        print(corner_space + stars)
k = n - 2
for i in range(1,n):
    corner_space = " " * (i)
    if(i<(n-1)):
        hollow_space = "  " * (k-i)
        print(corner_space + "* " + hollow_space + "* ")
    else:
        print(corner_space + "*")