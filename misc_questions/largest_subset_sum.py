
def largest_subset_sum(original_array, number_array, index, curr_sum):

    if index >= len(original_array):
        return curr_sum

    # include the current number
    number_array.append(original_array[index])
    sum1 = largest_subset_sum(original_array, number_array, index + 1, curr_sum + original_array[index])

    # exclude the current number, and restart
    sum2 = largest_subset_sum(original_array, [], index + 1, original_array[index])

    # print(f"{number_array} - sum {sum(number_array)}")
    return max(sum1, sum2, curr_sum)

if __name__ == "__main__":
    answer = largest_subset_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4], [], 0, 0)
    print(answer)
