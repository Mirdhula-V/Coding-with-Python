m = int(input())
n = int(input())

if m > n:
    greatest_num = m 
else:
    greatest_num = n 
lcm_found = False

for i in range(greatest_num,(m*n + 1)):
    if not lcm_found:
        if((i % m) == 0 and (i % n) == 0):
            lcm_found = True
            lcm = i 
print(lcm)