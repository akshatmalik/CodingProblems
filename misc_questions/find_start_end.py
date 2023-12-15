def start_end(nums, target):
    low = 0
    high = len(nums) - 1

    low_start = 0
    while low <= high:
        mid = int(low + (high - low) / 2)
        if nums[mid] == target:
            high = mid - 1
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        if nums[low] == target:
            break
    low_start = low

    high_end = 0
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if nums[mid] == target:
            low = mid + 1
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        if nums[high] == target:
            break
    high_end = high

    print(f"low_start {low_start} high_end {high_end}")

    return [low_start, high_end]

if __name__ == "__main__":
    assert start_end([5, 7, 7, 8, 8, 10], 8) == [3, 4]
