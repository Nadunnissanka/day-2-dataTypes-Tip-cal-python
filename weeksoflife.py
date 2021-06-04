age = int(input("Enter your current age: "))

#weeks
weeks_u_lived = age * 52
weeks_u_ninety = 90 * 52
weeks_u_have_to_live = weeks_u_ninety - weeks_u_lived

#days
days_u_lived = age * 365
days_u_ninty = 90 * 365
days_u_have_to_live = days_u_ninty - days_u_lived

#months
months_u_lived = age * 12
months_u_ninty = 90 * 12
months_u_have_to_live = months_u_ninty - months_u_lived

print(f"You have {round(days_u_have_to_live)} days, {round(weeks_u_have_to_live)} weeks and {round(months_u_have_to_live)} months to live.")

