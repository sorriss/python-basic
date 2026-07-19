from typing import Dict, List, Tuple

# Тіпізація для контактів, аргументів команд та розпарсеного вводу
Contacts = Dict[str, str]
CommandArgs = List[str]
ParsedInput = Tuple[str, CommandArgs]

# Функції для обробки команд
def parse_input(user_input: str) -> ParsedInput:
    # Розділення вводу користувача на команду та аргументи
    parts = user_input.strip().split()

    # Перевірка на порожній ввід
    if not parts:
        return "", []

    # Витягування команди та аргументів
    command = parts[0].lower()
    args = parts[1:]

    # Повернення розпарсеного вводу
    return command, args

# Функції додачі контакту
def add_contact(args: CommandArgs, contacts: Contacts) -> str:
    # Перевірка на правильну кількість аргументів
    if len(args) != 2:
        return "Invalid command. Usage: add <name> <phone>"

    # Витягування імені та телефону з аргументів
    name = args[0]
    phone = args[1]
    # Додавання контакту до словника
    contacts[name] = phone
    # Повернення повідомлення про успішне додавання контакту
    return f"Contact {name} added."

# Функції зміни контакту
def change_contact(args: CommandArgs, contacts: Contacts) -> str:
    # Перевірка на правильну кількість аргументів
    if len(args) != 2:
        return "Invalid command. Usage: change <name> <new_phone>"

    # Витягування імені та нового телефону з аргументів
    name = args[0]
    new_phone = args[1]

    # Перевірка наявності контакту та оновлення телефону
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    else:
        return f"Contact {name} not found."

# Функції показу телефону контакту
def show_phone(args: CommandArgs, contacts: Contacts) -> str:
    # Перевірка на правильну кількість аргументів
    if len(args) != 1:
        return "Invalid command. Usage: phone <name>"

    # Витягування імені з аргументів
    name = args[0]

    # Перевірка наявності контакту та повернення телефону
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."

# Функції показу всіх контактів
def show_all(contacts: Contacts) -> str:
    # Перевірка наявності контактів
    if not contacts:
        return "No contacts found."

    # Формування рядка з усіма контактами
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    # Ініціалізація словника контактів
    contacts: Contacts = {}
    print("Welcome to the assistant bot!")

    # Запуск циклу для обробки команд користувача
    while True:
        # Отримання вводу користувача
        user_input = input("Enter a command: ")
        # Розпарсення вводу користувача
        command, args = parse_input(user_input)

        # Перевірка команди та виклик відповідної функції
        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
