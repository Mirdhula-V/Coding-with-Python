n = int(input())

for i in range(1,n+1):
    space = "  " * ((n * 2) - (i + i))
    print(("* " * i) + space + ("* " * i))
for j in range(1,n):
    space = "  " * (j * 2)
    print(("* " * (n-j)) + space + ("* " * (n-j)))