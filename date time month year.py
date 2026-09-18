import datetime

now = datetime.datetime.now()

print("Date:", now.date())
print("Time:", now.strftime("%H:%M:%S"))
print("Year:", now.year)
print("Month:", now.month)