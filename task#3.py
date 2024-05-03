import re

def normalize_phone(phone_number):
    cleaned_phone_number = phone_number.strip()
    if cleaned_phone_number.startswith('+') or cleaned_phone_number.startswith('380'):
        cleaned_phone_number ="+" + re.sub(r'\D', '', cleaned_phone_number)
    else:
        cleaned_phone_number ="+38" + re.sub(r'\D', '', cleaned_phone_number)
    return cleaned_phone_number

    

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)