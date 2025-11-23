"""
Lab 01: CLI Application - PATCH3 VERSION - EDITED IN MAIN BRANCH
This version was edited directly in GitHub main branch
"""

def main(
    name: str, 
    lastname: str = "", 
    formal: bool = False
) -> None:
    """
    SAYS HELLO TO USER, OPTIONALLY USING LASTNAME AND FORMAL STYLE
    
    ARGS:
        NAME (STR): USER NAME (REQUIRED)
        LASTNAME (STR): USER LASTNAME (OPTIONAL) 
        FORMAL (BOOL): FORMAL GREETING FLAG (OPTIONAL)
    
    RETURNS:
        NONE: PRINTS GREETING TO CONSOLE
    """
    # CHECK GREETING MODE
    if formal:
        # FORMAL GREETING WITH LASTNAME
        greeting = f"Добрый день, {name} {lastname}!"
    else:
        # INFORMAL GREETING WITH NAME ONLY
        greeting = f"Привет, {name}!"
    
    # PRINT THE GREETING
    print(greeting)


if __name__ == "__main__":
    import argparse
    
    # COMMAND LINE ARGUMENTS PARSING
    parser = argparse.ArgumentParser(
        description="Говорит 'Привет' пользователю"
    )
    
    parser.add_argument(
        "name", 
        help="Имя пользователя"
    )
    
    parser.add_argument(
        "--lastname", 
        default="", 
        help="Фамилия пользователя."
    )
    
    parser.add_argument(
        "--formal", 
        "-f", 
        action="store_true", 
        help="Использовать формальное приветствие."
    )
    
    # GET ARGUMENTS AND CALL MAIN FUNCTION
    arguments = parser.parse_args()
    main(arguments.name, arguments.lastname, arguments.formal)
