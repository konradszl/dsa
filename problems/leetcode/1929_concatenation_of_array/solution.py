def get_concatenation(nums: list[int]) -> list[int]:
    result = [0] * len(nums) * 2

    for i, num in enumerate(nums):
        result[i] = num
        result[i + len(nums)] = num

    return result
