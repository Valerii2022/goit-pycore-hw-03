from datetime import datetime

def get_days_from_today(date):
    try:
        received_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        days_count = current_date - received_date
        return f"Кількість днів між поточною та заданою датами: {days_count.days}"
    except ValueError:
        return "Дата має бути у форматі 'РРРР-ММ-ДД'"
    except TypeError:
        return "Невірний тип переданих даних"


# days_count = get_days_from_today("20-13-05")
# days_count = get_days_from_today("dfgdfg")
# days_count = get_days_from_today(2024)
days_count = get_days_from_today("2023-05-03")
print(days_count)
