def sum_of_two_bigger_than_third(num1: int, num2: int, num3: int) -> bool:
    """
    Checks if sum of first to integers is >= 3rd num.
    Params:
        num1 (int): 1st number of sum
        num2 (int): 2nd number of sum
        num3 (int): 3rd number to compare to
    Returns:
        (bool): True, if condition is met, else False
    """
    return num1 + num2 >= num3


if __name__ == "__main__":
    print(sum_of_two_bigger_than_third(2, 2, 5))
