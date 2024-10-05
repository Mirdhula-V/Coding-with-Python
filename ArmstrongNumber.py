Number = input()

first_digit = Number[0]
first_digit = int(first_digit)

second_digit = Number[1]
second_digit = int(second_digit)

third_number = Number[2]
third_number = int(third_number)

Number = int(Number)

cube_of_first_digit = first_digit ** 3
cube_of_second_digit = second_digit ** 3
cube_of_third_digit = third_number ** 3

sum_of_cube = cube_of_first_digit + cube_of_second_digit + cube_of_third_digit

if (sum_of_cube == Number):
    print("True")
else:
    print("False")