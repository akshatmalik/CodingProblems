def sum_of_three(nums, i, j, k, sum, target_sum):
    if i == j or j == k or i == j == k or i >= len(nums) or j >= len(nums) or k >= len(nums):
        return False

    if target_sum == sum:
        return True

    sum1 = sum_of_three(nums, i + 1, j, k, nums[i] + nums[j] + nums[k], target_sum)
    sum2 = sum_of_three(nums, i, j + 1, k, nums[i] + nums[j] + nums[k], target_sum)
    sum3 = sum_of_three(nums, i, j, k + 1, nums[i] + nums[j] + nums[k], target_sum)

    return any([sum1, sum2, sum3])


if __name__ == "__main__":
    assert sum_of_three([3, 7, 1, 2, 8, 4, 5], 0, 1, 2, 3 + 7 + 1, 10) == True
    assert sum_of_three([2, 4, 2, 7, 6, 3, 1], 0, 1, 2, 2 + 4 + 2, 8) == True
