def check_two_number_sum_slowest(num_array, result_sum):
    for i in range(len(num_array) - 1):
        first_number = num_array[i]
        for j in range(i + 1, len(num_array) - 1):
            second_number = num_array[j]
            if first_number + second_number == result_sum:
                return [first_number, second_number]
    return []


def find_pair(array, target_sum, left_key, right_key):

    if left_key > right_key:
        return []

    current_sum = array[left_key] + array[right_key]

    if current_sum == target_sum:
        return [array[left_key], array[right_key]]

    elif current_sum > target_sum:
        right_key -= 1
        return find_pair(array, target_sum, left_key, right_key)

    elif current_sum < target_sum:
        left_key += 1
        return find_pair(array, target_sum, left_key, right_key)


def check_two_numbers_medium(array, target_sum):
    array.sort()
    left_key = 0
    right_key = len(array) - 1
    return find_pair(array, target_sum, left_key, right_key)


if __name__ == '__main__':
    string_array_input = input("Enter Array\n").split(' ')
    input_array = [int(num) for num in string_array_input]
    input_sum = int(input("Enter the expected sum\n"))
    print(check_two_numbers_medium(input_array, input_sum))