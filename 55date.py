import datetime
today = datetime.date.today()
ten_days = datetime.timedelta(days=10)
# Calculate future and past dates
future_date = today + ten_days
past_date = today - ten_days
print("Date after 10 days:", future_date)
print("Date 10 days ago:", past_date)