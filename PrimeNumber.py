N = int(input())
no_of_factors = 0

for i in range(2,N):
    if(N%i == 0):
        no_of_factors = no_of_factors + 1 

if(no_of_factors==0):
    print("Prime Number")
else:
    print("Not a Prime Number")