n = int(input())
count = 1 
for i in range(1,n+1):
    result = ""
    for j in range(1,i+1):
        result = result + str(count) + " "
        count = count + 1 
    print(result)