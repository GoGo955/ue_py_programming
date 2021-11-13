# 2a
def print_5_names(list_with_names: list):
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

# 2b i
def list_elements_by2_for(list_with_nums: list):
    """
    Function multiplies by 2 each element of 5 element list.
    Arguments:
        list_with_nums (list): list with numbers to transform
    Returns:
        transformed_list (list): list with elements multiplied by 2
    """
    if (list_len := len(list_with_nums)) != 5:
        print(f'Length of list is {list_len}, while it should be 5!')
        return list_with_nums
    else:
        for number in range(len(list_with_nums)):
            list_with_nums[number] *=2
        return list_with_nums

# 2b ii
def list_elements_by2_compreh(list_with_nums: list):
    """
    Function multiplies by 2 each element of 5 element list.
    Arguments:
        list_with_nums (list): list with numbers to transform
    Returns:
        transformed_list (list): list with elements multiplied by 2
    """
    if (list_len := len(list_with_nums)) != 5:
        print(f'Length of list is {list_len}, while it should be 5!')
        return list_with_nums
    else:
        return [num*2 for num in list_with_nums]

# 2c + 2d
def for_with_range():
    """
    First loop prints elements divisible by 2.
    Second loop prints every second element of 
    the list.
    Arguments:
        No arguments
    Returns:
        Does not return anything
    """
    # prints every element divisible by 2
    for i in range(0,10):
        if i%2 == 0:
            print(i)
    print('\n')
    # prints every second element
    for i in range(1,11,2):
    # for i in range(1,11)[::2]:
        print(i)

if __name__ == "__main__":
    print_5_names(['dan','ban'])
    print_5_names(['dan','ban','ran','man','pan'])
    print(list_elements_by2_for([1,3]))
    print(list_elements_by2_for([1,1,1,1,1]))
    print(list_elements_by2_compreh([1,3]))
    print(list_elements_by2_compreh([1,1,1,1,1]))
    for_with_range()
