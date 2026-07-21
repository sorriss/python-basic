import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_tree(path: Path, prefix: str = "") -> None:
    # Отримання списку файлів та директорій у поточній директорії
    try:
        items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except PermissionError:
        print(f"Error: permission denied for {path}.")
        return
    except FileNotFoundError:
        print(f"Error: {path} no longer exists.")
        return
    except NotADirectoryError:
        print(f"Error: {path} is not a directory.")
        return
    except OSError as error:
        print(f"Error accessing {path}: {error}")
        return

    # Виведення файлів та директорій
    for i, item in enumerate(items):
        # Перевірка, чи є елемент останнім у списку
        is_last = i == len(items) - 1
        # Визначення символу з'єднання та префіксу для наступного рівня
        connector = "└── " if is_last else "├── "
        # Визначення префіксу для наступного рівня
        next_prefix = prefix + ("    " if is_last else "│   ")

        # Перевірка на директорію
        if item.is_dir():
            # Виведення назви директорії з кольором
            print(f'{prefix}{connector}{Fore.BLUE}{item.name}/{Style.RESET_ALL}')
            # Рекурсивний виклик функції для виведення вмісту директорії
            print_tree(item, next_prefix)
        else:
            # Виведення назви файлу з кольором
            print(f"{prefix}{connector}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

def main() -> None:
    # Ініціалізація colorama
    init(autoreset=True)

    # Перевірка аргументів командного рядка
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Usage: python 6.3.py <directory_path> (use 'python 6.3.py .venv' to fast example)")
        sys.exit(1)

    # Отримання шляху до директорії
    dir_path = Path(sys.argv[1])

    # Перевірка, чи існує шлях і чи вказує він на директорію
    if not dir_path.exists():
        print(Fore.RED + f"Error: {dir_path} does not exist.")
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + f"Error: {dir_path} is not a directory.")
        sys.exit(1)

    # Виведення дерева директорії
    print(Fore.CYAN + f"{dir_path.name}/")
    print_tree(dir_path)

if __name__ == "__main__":
    main()
