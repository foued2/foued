from typing import List


class Solution:
    @staticmethod
    def searchRange(nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        """ 
        A sequence of values is said to be in non-decreasing order if the successive element is greater than
        or equal to its previous element in the sequence.
        This order occurs when the sequence contains duplicate values.
        """
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        res = [-1, -1]

        if nums[mid] == target:
            res = [mid, mid]
        while low < mid < high:
            if nums[low] < target:
                low += 1
            else:
                res[0] = low
            if nums[high] > target:
                high -= 1
            else:
                res[1] = high
        if len(nums) == 2 and nums[1] == target:
            if nums[0] == target:
                return [0, 1]
            else:
                return [1, 1]
        if target not in nums:
            return [-1, -1]
        return res

    print(searchRange(nums=[1, 1, 1, 1, 2, 2], target=2))
