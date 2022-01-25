# Life in Weeks
while True:
# getting age from the user
    age = int(input("Enter your Age in years: "))

# #let us assume the averae age of humans is 90 years.

#     average_age_in_years = 90
#     average_age_in_weeks = average_age_in_years*52
#     average_age_in_days = average_age_in_years*365
#     average_age_in_months = average_age_in_years*12

# # Calculating age of User

#     user_age_in_days = average_age_in_days - (age*365)
#     user_age_in_weeks = average_age_in_weeks - (age*52)
#     user_age_in_years = average_age_in_years - age
#     user_age_in_months = average_age_in_months - (age*12)

#     print(f"\n average human life is {average_age_in_years} years,{average_age_in_months} Months,{average_age_in_weeks} weeks,{average_age_in_days} days \n")

#     print(f" you have {user_age_in_days} days,{user_age_in_weeks} weeks, and {user_age_in_months} months left. \n")

    years_remaining = 90 - age
    age_in_months = years_remaining * 12
    age_in_weeks = years_remaining * 52
    age_in_days = years_remaining * 365

    users_left_overage = f"you have {age_in_months} Months, {age_in_weeks} Weeks, {age_in_days} Days Remaining"

    print(users_left_overage)