# This has O(n) time as we are looping through the complete main array list in a worst case scenario
# This has O(1) space

def validate_subsequence(main_array, sequence):
    main_arr_idx = sequence_idx = 0
    while main_arr_idx < len(main_array) and sequence_idx < len(sequence):
        if main_array[main_arr_idx] == sequence[sequence_idx]:
            sequence_idx += 1
        main_arr_idx += 1
    return sequence_idx == len(sequence)


validate_subsequence([1, 2, 233, 5, 23], [1, 5, 4, 23])


# This has O(n) time as we are looping through the complete main array list in a worst case scenario
# This has O(1) space

def validate_subsequence(main_array, sequence):
    sequence_index = 0
    for ele in main_array:
        if sequence_index == len(sequence):
            break
        if ele == sequence[sequence_index]:
            sequence_index += 1
    return sequence_index == len(sequence)


validate_subsequence([1, 2, 233, 5, 23], [1, 5, 23])
