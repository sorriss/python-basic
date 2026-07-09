import re

def normalize_phone(phone_numbr):
    prep_number = re.sub(r'[^\d+]', '', phone_numbr) # Тільки цифри та знак +

    if prep_number.startswith('+'): # Якщо номер починається з плюса то повертаємо його
        return prep_number

    if prep_number.startswith('380'): # Якщо номер починається з 380 то додаємо +
        return '+' + prep_number

    return '+38' + prep_number # У всіх ішхи випадках додаємо +38

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
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