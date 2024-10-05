String = input()
upper_string = String.upper()

length = len(String)
length = int(length)

new_string = ""

for i in range(1,length+1):
    new_string = new_string + String[length-i]
    result = new_string.upper()
    
if(upper_string == result):
    print("Palindrome")
else:
    print("Not a Palindrome")