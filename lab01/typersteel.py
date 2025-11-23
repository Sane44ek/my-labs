"""
CLI application compatible with the assignment requirements
Uses argparse as fallback when typer is not available
"""

def main(name: str, lastname: str = "", formal: bool = False):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Говорит 'Привет' пользователю")
    parser.add_argument("name", help="Имя пользователя")
    parser.add_argument("--lastname", default="", help="Фамилия пользователя.")
    parser.add_argument("--formal", "-f", action="store_true", 
                       help="Использовать формальное приветствие.")
    
    args = parser.parse_args()
    main(args.name, args.lastname, args.formal)
