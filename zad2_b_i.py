# 2b i
def list_elements_by2_for(list_with_nums: list) -> list:
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
        for idx, number in enumerate(list_with_nums):
            list_with_nums[idx] *=2
        return list_with_nums

if __name__ == "__main__":
    print(list_elements_by2_for([1,3]))
    print(list_elements_by2_for([1,2,3,4,5]))