Year = int(input())

is_divisible_by_400 = (Year % 400) == 0 
is_divisible_by_4 = (Year % 4) == 0 and (Year % 10) != 0

if (is_divisible_by_4 or is_divisible_by_400):
    print("True")
else: 
    print("False")