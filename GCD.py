m = int(input())
n = int(input())

if m > n:
    largest_num = m 
else:
    largest_num = n 
gcd = largest_num

for i in range(1,largest_num + 1):
    if (n % i == 0) and (m % i == 0):
        gcd = i 
print(gcd)