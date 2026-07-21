from typing import TypedDict
from pathlib import Path as path

# типізація словника для інформації про кота
class CatInfo(TypedDict):
    id: str
    name: str
    age: str

def get_cats_info(path: str) -> list[CatInfo]:
    cats: list[CatInfo] = []

    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                # Перевірка на пустий рядок
                if not line:
                    continue

                # Розділяємо рядок на частини
                parts = line.split(',')

                # Перевірка на наявність трьох частин (id, name, age)
                if len(parts) != 3:
                    continue

                # Створюємо словник з інформацією про кота
                cat_info: CatInfo = {
                    'id': parts[0],
                    'name': parts[1],
                    'age': parts[2]
                }

                # Додаємо словник до списку котів
                cats.append(cat_info)

    # Обробка помилок при відкритті файлу
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except ValueError:
        raise ValueError(f"Invalid data in file: {path}")

    return cats

if __name__ == "__main__":
    data_file_str = str(path(__file__).parent / "6.2.data.txt")
    cats_info = get_cats_info(data_file_str)
    print(cats_info)