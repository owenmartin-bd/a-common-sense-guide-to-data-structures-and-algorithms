def linear_search(array, search_value):
    i = 0
    while i < len(array):
        if array[i] == search_value:
            return f'Value: {array[i]}, index:{i}'
        elif array[i] > search_value:
            break
        i += 1
    return 'The value does not exists.'

arr = [1, 13, 38, 75, 101, 151]

print(linear_search(arr, 38))
print(linear_search(arr, 78))