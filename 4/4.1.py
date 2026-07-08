from datetime import datetime

def get_days_from_today(days):
    try: # Спроба обробки вхідних даних
        given_date = datetime.strptime(days, '%Y-%m-%d').date() # Превожу строку в об'єкт datetime
        today = datetime.today().date() # Отримую datetime для сьогоднішнього дня

        return (today - given_date).days # Отримую timedelta між датами

    except ValueError: # Обробка помилики
        return "Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'."


print(get_days_from_today("2025-07-08"))
print(get_days_from_today("2027-07-08"))
print(get_days_from_today("2028+10+09"))