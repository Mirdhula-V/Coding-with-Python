T = input()

float_temp = float(T[:-1])
char_in_T = T[-1]

if char_in_T == "C":
    print(str(float_temp) + "C")
    print(str(round((9 * float_temp) / 5 + 32 , 2))  + "F")
    print(str(round(float_temp + 273 , 2)) + "K")
    
elif char_in_T == "F":
    print(str(round((float_temp - 32) * 5 / 9 , 2)) + "C")
    print(str(float_temp) + "F")
    print(str(round((float_temp - 32) * 5 / 9 + 273 , 2)) + "K")
    
elif char_in_T == "K":
    print(str(round(float_temp - 273 , 2)) + "C")
    print(str(round((float_temp - 273) * 9 / 5 + 32 , 2)) + "F")
    print(str(float_temp) + "K")