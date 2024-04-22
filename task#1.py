from datetime import datetime

def get_days_from_today(date:str) -> str:
    try:
        received_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        days_count = (current_date - received_date).days
        return f"Кількість днів між поточною та заданою датами: {days_count}"
    except ValueError:
        return "Дата має бути у форматі 'РРРР-ММ-ДД'"

print(get_days_from_today("2025-04-20"))
