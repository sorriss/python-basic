from datetime import datetime, timedelta, date

def get_upcoming_birthdays(users):
    today = datetime.today().date()  # Отримую сьогоднішню дату
    upcoming = []  # Список для збереження користувачів

    for user in users:
        name = user['name']
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже пройшов цього року, використовую наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Розраховую різницю в днях між сьогоднішньою датою та днем народження
        days_diff = (birthday_this_year - today).days

        # Перевіряю, чи день народження користувача відбудеться протягом наступних 7 днів
        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:  # Якщо день народження в суботу
                congratulation_date += timedelta(days=2)  # Переносимо на понеділок
            elif congratulation_date.weekday() == 6:  # Якщо день народження в неділю
                congratulation_date += timedelta(days=1)  # Переносимо на понеділок

            upcoming.append({
                'name': name,
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming

users = [
    {"name": "John Doe", "birthday": "1985.07.15"},
    {"name": "Jane Smith", "birthday": "1990.07.19"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)