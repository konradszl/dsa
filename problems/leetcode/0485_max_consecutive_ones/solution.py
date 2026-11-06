def find_max_consecutive_ones(nums: list[int]) -> int:
    count = 0
    result = 0

    for num in nums:
        if num:
            count += 1
        else:
            count = 0

        result = max(result, count)

    return result
