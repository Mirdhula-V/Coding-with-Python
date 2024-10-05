n = int(input()) 

for i in range(1,n+1):
    mid_space = ("  " * (2 * (n-i)))
    if(i==1):
        print("* " + mid_space + "* ")
    else:
        hollow_space = "  " * (i-2)
        print("* " + hollow_space + "* " + mid_space + "* " + hollow_space + "* ")
   
for i in range(1,n+1):
    mid_space = ("  " * (2 * (i - 1)))
    if(i<n):
        hollow_space = "  " * (n-i-1)
        print("* " + hollow_space + "* " + mid_space + "* " + hollow_space + "* ")
    else:
        print("* " + mid_space + "* ")