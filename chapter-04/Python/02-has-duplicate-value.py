def hasDuplicateValue(array):
    existing_numbers = {}
    for num in array:
        if existing_numbers.get(num) == 1:
            return True
        else:
            existing_numbers[num] = 1
    return False

print(hasDuplicateValue([1,2,3,4,1,2]))