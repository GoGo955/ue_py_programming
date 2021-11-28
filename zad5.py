def int_in_list(list_to_check: list, num: int) -> bool:
    """
    Checks if int is in list.
    Params:
        list_to_check (list): list to check
        num (int): num to check if in list
    Returns:
        (bool): 
    """
    return num in list_to_check


if __name__ == "__main__":
    print(int_in_list([1, 2, 3], 4))
    print(int_in_list([1, 2, 3], 2))
