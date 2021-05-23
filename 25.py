import datetime

today = datetime.date.today()
print('today:',today)
tommorrow=today + datetime.timedelta(days=1)
print("tommorrow", tommorrow)
yesterday = today-datetime.timedelta(days=1)
print("yesterday:",yesterday)
print("diff:",tommorrow-yesterday)
