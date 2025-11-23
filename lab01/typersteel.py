"""
Lab 01: CLI Application with formal/informal greetings
Author: Sane44ek
Date: 2025
Description: Implementation of CLI with argparse fallback
"""

def main(name: str, lastname: str = "", formal: bool = False):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    
    Args:
        name (str): Имя пользователя (обязательный параметр)
        lastname (str): Фамилия пользователя (опционально)
        formal (bool): Флаг формального приветствия (опционально)
    
    Returns:
        None: Выводит приветствие в консоль
    """
    # Проверяем режим приветствия
    if formal:
        # Формальное приветствие с фамилией
        print(f"Добрый день, {name} {lastname}!")
    else:
        # Неформальное приветствие только с именем
        print(f"Привет, {name}!")

if __name__ == "__main__":
    import argparse
    
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Говорит 'Привет' пользователю")
    parser.add_argument("name", help="Имя пользователя")
    parser.add_argument("--lastname", default="", help="Фамилия пользователя.")
    parser.add_argument("--formal", "-f", action="store_true", 
                       help="Использовать формальное приветствие.")
    
    # Получаем аргументы и вызываем основную функцию
    args = parser.parse_args()
    main(args.name, args.lastname, args.formal)
