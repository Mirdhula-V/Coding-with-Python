n = int(input())

print("* " * (2 * n - 1))
for i in range(1,n):
    l_space = " " * (i)
    h_space = "  " * (i - 1)
    star = "* " * (n - i)
    print(l_space + star + h_space + star)