from datetime import date, datetime
def get_days_from_today(start_date):
    end_date = datetime.today()
    diff = (end_date - start_date).days
    return diff
start_date = datetime(1992,8,6)
result = get_days_from_today(start_date)
print(result)
