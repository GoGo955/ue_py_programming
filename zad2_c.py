def for_with_range() -> None:
    """
    Loop prints elements divisible by 2.
    Arguments:
        No arguments
    Returns:
        Does not return anything
    """
    # prints every element divisible by 2
    for i in range(0,10):
        if i%2 == 0:
            print(i)

if __name__ == "__main__":
    for_with_range()