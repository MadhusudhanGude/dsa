# O(Nlog(N))T
# O(N)S
def sorted_square_array(array):
    result = []
    for ele in array:
        ele_square = ele * ele
        result.append(ele_square)
    result.sort()
    return result


print(sorted_square_array([-4, -1, 2, 11, 16]))


# O(N)T
# O(1)S
def sorted_square_array(array):
    result = [0] * len(array)
    lowest_value_index = 0
    highest_value_index = len(array) - 1

    for index in reversed(range(len(array))):
        smallest_value = array[lowest_value_index]
        highest_value = array[highest_value_index]
        if abs(smallest_value) > abs(highest_value):
            result[index] = smallest_value * smallest_value
            lowest_value_index += 1
        else:
            result[index] = highest_value * highest_value
            highest_value_index -= 1
    return result


print(sorted_square_array([-4, -1, 2, 11, 16]))
