import random

def get_numbers_ticket(min, max, quantity):
    isMinMaxValid = min < 1 or max > 1000 or min > max # Перевірка min max
    isQuantityValid = quantity < 1 or quantity > max - min + 1 # Перевірка quantity

    if isMinMaxValid or isQuantityValid: # Числа не повертаються якщо не вірні параметри
        return []

    numbers = random.sample(range(min, max + 1), quantity) # Генерація (range) та обирання (sample) унікальних випадкових чисел

    return sorted(numbers) # Сортування чисел

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers1 = get_numbers_ticket(10, 999, 16)
print("Ваші лотерейні числа1:", lottery_numbers1)

lottery_numbers2 = get_numbers_ticket(-1, 999, 16)
print("Ваші лотерейні числа2:", lottery_numbers2)

lottery_numbers3 = get_numbers_ticket(1, 1999, 16)
print("Ваші лотерейні числа3:", lottery_numbers3)