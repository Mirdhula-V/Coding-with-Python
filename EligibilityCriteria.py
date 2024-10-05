M = int(input())
P = int(input())
C = int(input())

condition_1 = (M >= 70) and (P >= 60) and (C >= 60)

condition_2 = ((M+P+C) >= 180 )

result = condition_1 or condition_2

print(result)