# Using HASH MAP
# O(N)S - as we are storing each element in dict
# O(N)T - as we are looping through the elements in an array

def find_two_num_sum(array, sum):
    hash_map = {

    }
    for element in array:
        expected_pair = sum - element
        if expected_pair in hash_map:
            return [element, expected_pair]
        hash_map[element] = True
    return []


find_two_num_sum([1, 2, 32, -23, 118, 11], 9)


# O(1)S - as we are not storing anything here
# O(Nlog(N))T + O(N)T ~= O(Nlog(N))T

def find_two_num_sum(array, sum):
    array.sort()  # assuming a best sorting technique like quick sort would do this O(Nlog(N))T
    # array = [-23, 1, 2, 11, 32, 118]
    left_index = 0
    right_index = len(array)-1

    # In worst case it will be O(N)T
    while left_index < right_index:
        calculated_sum = array[left_index] + array[right_index]
        if calculated_sum < sum:
            left_index += 1
        elif calculated_sum > sum:
            right_index -= 1
        else:
            return [array[left_index], array[right_index]]

    return []


find_two_num_sum([1, 2, 32, -23, 118, 11], 9)
