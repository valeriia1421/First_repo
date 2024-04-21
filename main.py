from datetime import date, timedelta

start_date = date(year=2023, day=12, month=10)
end_date = date(year=2023, day=25, month=10)

diff = (end_date - start_date).days + 1

for i in range(diff):
    res = start_date + timedelta(days=i)
    print(res.strftime("%Y-%m-%d"))

