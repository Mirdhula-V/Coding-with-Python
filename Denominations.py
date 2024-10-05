A = int(input())

five_hundred = int(A/500)
fifties = int((A%500)/50)
tens = int(((A%500)%50)/10)
ones = int(((A%500)%50)%10)

print("500: " + str(five_hundred) + " " + "50: " + str(fifties) + " " + "10: " + str(tens) + " " + "1: " + str(ones))