import random

def get_numbers_ticket(min:int, max:int, quantity:int):
    try:
        if min < 1 or max >1000 or min > max:
            return "Діапазон чисел має бути від 1 до 1000."
        if quantity > max:
            return "Кількість чисел в унікальному списку має бути не більше максимального показника діапазону."
        lottery_numbers = set()
        while len(lottery_numbers) < quantity:
            lottery_numbers.add(random.randint(min, max))
        result = sorted(list(lottery_numbers))
        return f"Ваші лотерейні числа: {result}"
    except TypeError:
        return "Всі параметри мають бути дійсним цілим числом"    
    
print(get_numbers_ticket("3", 10, 2))
print(get_numbers_ticket(10, 10, 2))
print(get_numbers_ticket(0, 10, 2))
print(get_numbers_ticket(0, 1005, 2))
print(get_numbers_ticket(1, 10, 20))
print(get_numbers_ticket(1, 100, 10))
