# tells us how many days, weeks, months we have left if we live until 90 years old.

age = int(input("What is your current age? "))
print()
years = 90 - age
days = (years * 365)
weeks = (years * 52)
months = (years * 12)

print(f"You have {days} days, {weeks} weeks, {months} months left")