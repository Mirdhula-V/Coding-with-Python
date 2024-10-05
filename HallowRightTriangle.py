n = int(input())

print("_" * (n + 1))
for i in range(n):
    print("|" + " " * (n - 1 - i) + "/")