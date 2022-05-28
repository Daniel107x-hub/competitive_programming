from typing import List


def two_sum(nums: List[int], target):
    nums_dict = dict()
    for index, num in enumerate(nums):
        nums_dict[str(num)] = index
    for index, num in enumerate(nums):
        rest = target - num
        try:
            rest_index = nums_dict[str(rest)]
            if rest_index != index:
                return [index, rest_index]
        except Exception as e:
            pass


if __name__ == '__main__':
    nums = [int(n) for n in input().split(" ")]
    target = int(input())
    result = two_sum(nums, target)
    print(result)