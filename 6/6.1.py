from pathlib import Path as path

def total_salary(path: str) -> tuple[int, int]:
    total = 0
    count = 0

    try:
        # Відкриваємо файл для читання
        with open(path, 'r') as file:
            # Читаємо кожен рядок у файлі
            for line in file:
                # Видаляємо пробіли на початку та в кінці рядка
                line = line.strip()

                # Перевірка на пустий рядок
                if not line:
                    continue

                # Розділяємо рядок на ім'я та зарплату
                pats = line.split(',')

                # Перевірка на наявність другої частини (зарплати)
                if len(pats) == 2:
                    try:
                        # Калькуляция
                        salary = int(pats[1])
                        total += salary
                        count += 1

                        # Обробка помилки даних зарплати
                    except ValueError:
                        raise ValueError(f"Invalid salary value: {pats[1]}")

    # Обробка помилок при відкритті файлу
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except ValueError:
        raise ValueError(f"Invalid data in file: {path}")

    # Калькуляция середньої зарплати
    average = total // count if count > 0 else 0
    return total, average

if __name__ == "__main__":
    data_file_str = str(path(__file__).parent / "6.1.data.txt")
    total, average = total_salary(data_file_str)
    print(f"Total Salary: {total}")
    print(f"Average Salary: {average}")