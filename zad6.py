def set_to_third(first_list: list, second_list: list) -> list:
    """
    Functions extend first list with second.
    Then it creates a set of it, and raise 2 each element to second power.
    Params:
        first_list (list): list to extend
        second_list (list):  extending list
    Returns
        list: final list
    """
    first_list.extend(second_list)
    return list({num ** 2 for num in first_list})


if __name__ == "__main__":
    print(set_to_third([1, 2, 3], [1, 2, 3, 4]))
