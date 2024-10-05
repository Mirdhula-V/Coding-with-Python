n = int(input())

for i in range(n):
    l_spaces = " " * (n - i - 1)
    h_spaces = " " * (2 * i)
    
    print(l_spaces + "/" + h_spaces + "\\")
    
for i in range(n):
    l_spaces = " " * (i)
    h_spaces = " " * (2 * (n - i - 1))
    
    print(l_spaces + "\\" + h_spaces + "/")