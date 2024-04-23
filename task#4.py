import random

def get_numbers_ticket(min_value, max_value, quantity):
    # Перевірка на валідність вхідних параметрів
    if not (1 <= min_value <= 1000 and 1 <= max_value <= 1000 and min_value < max_value):
        return []  # Повертаємо порожній список, якщо параметри не валідні
    if not (min_value <= quantity <= max_value):
        return []  # Повертаємо порожній список, якщо кількість не у межах

    # Переконайтесь, що діапазон достатньо великий для кількості
    if (max_value - min_value + 1) < quantity:
        return []  # Повертаємо порожній список, якщо діапазон не достатньо великий

    # Використання множини для зберігання унікальних чисел
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_value, max_value))

    # Перетворення на список та сортування
    sorted_numbers = sorted(list(numbers_set))
    return sorted_numbers


# Приклад використання
min_value = "1"
max_value = 49
quantity = 6

ticket = get_numbers_ticket(min_value, max_value, quantity)
print("Випадковий лотерейний квиток:", ticket)