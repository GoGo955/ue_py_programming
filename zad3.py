def divisible_by_2(num1: int) -> bool:
    """
    Function tells you if your number is divisible by 2.
    Params:
        num (int): number to check
    Returns:
        (bool): True if divisible, else False
    """
    return num1 % 2 == 0


if __name__ == "__main__":

    if divisible_by_2(5):
        print('Liczba parzysta')
    else:
        print('Liczba nieparzysta')
