def contains_duplicate(nums):
    nums_dict = dict()
    for num in nums:
        num_in_map = nums_dict.get(num)
        if num_in_map is not None:
            return True
        nums_dict[num] = num
    return False

if __name__ == '__main__':
    nums = [int(n) for n in input().split(" ")]
    result = contains_duplicate(nums)
    print(result)