import datetime

birthyear = int(input("Enter your birth year: "))
today = datetime.date.today()
current_year = today.year
age = current_year - birthyear
print(f"Your age is {age}")