"""
Author: Kara Meyer
Date: 10-30-2019
Description: This program balances weights

REQUIREMENTS:
* This code takes in a string array (named strArr) with the first element
containing the values of the two weights on the scale, and the second element
being the miscellaneous weights. For example, when strArr =
["[5, 9]", "[1, 2, 6, 7]"] the left weight is 5, the right weight is 9, and
the weights that could be added to the scale are 1, 2, 6, and 7.
* All numbers in the string array must be positive integers.
* The goal is the balance the scale by using the least amount of weights from
the list, but using at most only 2 weights. In the example used above, the
scale could be balanced by adding 6 to the left side and 2 to the right side.
* The prgram should return a comma separated string of the weights that were
used from the list in ascending order, so for this example your program should
return the string "2,6".
* There will only ever be one unique solution and the list of available
weights will not be empty.
* It is also possible to add two weights to only one side of the scale to
balance it.
* If it is not possible to balance the scale then your program should return
the string "not possible".
* The format of the strArr must be exactly ["[left, right]", "[1, 2, 3]"] for
the program to work.
"""


def convert_int_list(strArr, index):
    """Convert comma delimited string into list of integers."""
    remove_brackets = strArr[index]
    remove_brackets = remove_brackets[1:-1]
    convert_to_list = remove_brackets.split(', ')
    string_to_int = [int(i) for i in convert_to_list]

    return string_to_int


def ascending_order(number, second_number):
    """Order the numbers in the list from smallest to largest."""
    if number < second_number:
        string = "{}, {}".format(number, second_number)
        return string
    else:
        string = "{}, {}".format(second_number, number)
        return string


def ScaleBalancing(strArr):
    """Balance a scale by adding a max of two weights."""
    # Put the first listed weights in the weights on scale list
    weights_on_scale = convert_int_list(strArr, 0)

    # Put the second listed weights in the other weights list
    other_weights = convert_int_list(strArr, 1)

    # Define our left and right side of the scale for testing
    left_scale = weights_on_scale[0]
    right_scale = weights_on_scale[1]

    # Check if only one weight is needed to balance
    for number in other_weights:
        left_scale += number
        if left_scale == right_scale:
            strArr = number
            return strArr
        left_scale = weights_on_scale[0]  # Reset left scale
        right_scale += number
        if left_scale == right_scale:
            strArr = number
            return strArr
        right_scale = weights_on_scale[1]  # Reset right scale

    # Check if putting two weights on opposite sides are needed to balance
    for index, number in enumerate(other_weights):
        left_scale += number
        for second_index, second_number in enumerate(other_weights):
            if index == second_index:  # Cannot reuse weights
                continue
            right_scale += second_number
            if left_scale == right_scale:
                strArr = ascending_order(number, second_number)
                return strArr
            right_scale = weights_on_scale[1]  # Reset right scale
        left_scale = weights_on_scale[0]  # Reset left scale

    # Check if putting two weights on one side are needed to balance
    for index, number in enumerate(other_weights):
        # Test adding the weights to the left
        left_scale += number
        for second_index, second_number in enumerate(other_weights):
            if index == second_index:  # Cannot reuse weights
                continue
            left_scale += second_number
            if left_scale == right_scale:
                strArr = ascending_order(number, second_number)
                return strArr
            left_scale -= second_number  # Reset left scale before 2nd weight
        left_scale = weights_on_scale[0]  # Reset left scale completely
        # Test adding weights to the right
        right_scale += number
        for second_index, second_number in enumerate(other_weights):
            if index == second_index:  # Cannot reuse weights
                continue
            right_scale += second_number
            if left_scale == right_scale:
                strArr = ascending_order(number, second_number)
                return strArr
            right_scale -= second_number  # Reset right scale before 2nd weight
        right_scale = weights_on_scale[1]  # Reset right scale completely

    # Return the string "not possible" if not possible to balance
    strArr = "not possible"
    return strArr


print(ScaleBalancing(["[5, 9]", "[1, 2, 6, 7]"]))
print(ScaleBalancing(["[3, 4]", "[1, 2, 7, 7]"]))
print(ScaleBalancing(["[13, 4]", "[1, 2, 3, 6, 14]"]))
