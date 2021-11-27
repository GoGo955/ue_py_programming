# 2a
def print_5_names(list_with_names: list) -> None:
    """
    Function prints names from given list with len 5.
    Arguments:
        list_with_names (list): list with names to print
    Returns:
        Does not return anything
    """
    if (list_len := len(list_with_names)) != 5:
        print(f'Length of list is {list_len}, while it should be 5!')
    else:
        for name in list_with_names:
            print(name)

if __name__ == "__main__":
    print_5_names(['dan','ban'])
    print_5_names(['dan','ban','ran','man','pan'])