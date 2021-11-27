def for_with_range() -> None:
    """
    Loop prints every second element of the list.
    Arguments:
        No arguments
    Returns:
        Does not return anything
    """
    # prints every second element
    for  idx, num in enumerate(range(1,11)):
        if idx % 2 == 0:
            print(num)

if __name__ == "__main__":
    for_with_range()