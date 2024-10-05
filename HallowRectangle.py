m = int(input())
n = int(input())

print("* " * n)

for i in range(1,m - 1):
    middle_space = "  " * (n - 2)
    row = "* " + middle_space + "* "
    print(row)
    
print("* " * n)