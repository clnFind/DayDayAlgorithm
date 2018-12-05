# -*- coding: utf-8 -*-
import copy


class Solution(object):
    """
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums_copy = copy.copy(nums)
            nums_copy.remove(nums[i])
            for j in nums_copy:
                if nums[i] + j == target:
                    return i, nums.index(j)
        return None

    def two_sum(self, nums, target):

        for num in nums:
            val = target - num
            if val in nums:
                return nums.index(num), nums.index(val)
        return None


if __name__ == '__main__':

    l = [3, 4, 10, 2, 7]
    target = 9
    result = Solution().twoSum(l, target)
    print(result)

    result1 = Solution().two_sum(l, target)
    print(result1)
