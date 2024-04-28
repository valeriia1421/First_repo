from datetime import date, datetime

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def valid_date(year, month, day):
    if year < 1:
        return False
    if not (1 <= month <= 12):
        return False
    day_counts = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not (1 <= day <= day_counts[month - 1]):
        return False
    return True

def get_days_from_today(year, month, day):
	if not valid_date(year, month, day):
		return "Invalid date"
	start_date = datetime(year, month, day)
	end_date = datetime.today()
	diff = (end_date - start_date).days
	return diff

result = get_days_from_today(1992,8,6)
print(result)

result = get_days_from_today(1992,30,6)
print(result)