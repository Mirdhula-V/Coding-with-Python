n = int(input())
k = int(input())

sum_of_numbers = 0

for i in range(1 , n+1):
    power = (i ** k)
    sum_of_numbers = sum_of_numbers + power
    
print(sum_of_numbers)