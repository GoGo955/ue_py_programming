def greet(name: str, surname: str) -> str:
    """
    Func greets.
    Params:
        nane (str): Person's name
        surname (str): Person's surname
    Returns:
        (str): greetings
    """
    return f'Czesc {name} {surname}'


if __name__ == "__main__":
    print(greet("bob", "ross"))
