n = int(input())

print("* " * n)

for i in range(1,n-1):
    middle_spaces = "  " * (n - 2)
    row = "* " + middle_spaces + "* "
    print(row)
print("* " * n)