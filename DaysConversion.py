Total_days = int(input())

years = int(Total_days / 365)
balance_of_years = Total_days - (365 * years)

weeks = int(balance_of_years / 7)
balance_of_weeks = balance_of_years - (7 * weeks)

days = balance_of_weeks

print(str(years) + " years " + str(weeks) + " weeks " + str(days) + " days")