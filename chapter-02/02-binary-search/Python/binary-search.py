import math
def binary_search(array, search_value):
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        mid_point = math.floor((lower_bound + upper_bound) / 2)
        value_at_mid_point = array[mid_point]
        if array[mid_point] == search_value:
            return f'Value: {search_value} found at the index: {mid_point}'
        elif search_value < value_at_mid_point:
            upper_bound = mid_point - 1
        elif search_value > value_at_mid_point:
            lower_bound = mid_point + 1

    return 'Value does not exists'

arr = [1, 23, 56, 87, 91, 101, 119, 137, 156, 178, 191]

print(binary_search(arr, 101))
print(binary_search(arr, 78))
        
