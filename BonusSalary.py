salary = int(input())
year_of_service = int(input())

if (year_of_service > 5):
    bonus = salary * 0.05
    print(bonus)
else:
    print("No Bonus")