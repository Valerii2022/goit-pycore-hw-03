from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.05.08"},
    {"name": "Jane Smith", "birthday": "1990.05.07"},
    {"name": "James Roney", "birthday": "1985.05.09"},
    {"name": "David James", "birthday": "1990.04.22"},
    {"name": "Jo Cole", "birthday": "1988.08.10"},
    {"name": "Steave Smith", "birthday": "1990.05.07"}
]

def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    current_week_ending = current_date + timedelta(7)
    print(current_date,current_week_ending)
    result:list = []
    for user in users:
        congratulation_date = datetime.strptime(user["birthday"], '%Y.%m.%d').replace(year=2024).date()
        result.append({"name":user["name"], "congratulation_date": f"{congratulation_date}"})
    return result


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

# congratulation_date