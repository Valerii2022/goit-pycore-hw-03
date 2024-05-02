from datetime import datetime

def get_days_from_today(date:str) -> str:
    try:
        received_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        days_count = current_date - received_date
        return f"Кількість днів між поточною та заданою датами: {days_count.days}"
    except ValueError:
        return "Дата має бути у форматі 'РРРР-ММ-ДД'"

# print(get_days_from_today("20-13-05"))
# print(get_days_from_today("dfgdfg"))
print(get_days_from_today("2021-05-05"))
