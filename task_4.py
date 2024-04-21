from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        name = user["name"]
        birthday_str = user["birthday"]
        
        year, month, day = map(int, birthday_str.split('.'))
        birthday_this_year = datetime(year=today.year, month=month, day=day).date()
        
        if birthday_this_year < today:
            birthday_this_year = datetime(year=today.year + 1, month=month, day=day).date()
        
        days_until_birthday = (birthday_this_year - today).days
        
        if 0 <= days_until_birthday <= 7:
            weekday = birthday_this_year.weekday()
            if weekday == 5: 
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif weekday == 6:
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year
            
            upcoming_birthdays.append({"name": name, "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    
    return upcoming_birthdays

users = [
    {"name": "Dima", "birthday": "1990.04.28"},
    {"name": "Lera", "birthday": "1992.04.25"},
    {"name": "Olesya", "birthday": "1985.05.01"},
    {"name": "Alex", "birthday": "1978.04.23"}
]

upcoming_birthdays=get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:",upcoming_birthdays)
