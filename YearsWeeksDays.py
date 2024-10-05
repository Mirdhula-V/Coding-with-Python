Total_days = int(input())

years = Total_days / 365
years = int(years)

days_years = 365 * years 

remaining_days_from_years = Total_days - days_years

months = remaining_days_from_years / 7
months = int(months)

days_months = 7 * months 

remaining_days_from_months = remaining_days_from_years - days_months

days = remaining_days_from_months

print(years)
print(months)
print(days)