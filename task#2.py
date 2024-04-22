import random

def get_numbers_ticket(min:int, max:int, quantity:int):
    lottery_numbers = []
    counter = 0
    while counter < quantity:
        lottery_numbers.append(random.randint(min, max))
        counter += 1
    print(f"Ваші лотерейні числа: {lottery_numbers}")
    return f"Ваші лотерейні числа: {lottery_numbers}"

get_numbers_ticket(1, 10,12)
