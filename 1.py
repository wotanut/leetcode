class Solution:
    """https://leetcode.com/problems/two-sum/"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for firstIndex, firstNum in enumerate(nums):
            for secondIndex, secondNum in enumerate(nums):
                if secondIndex == firstIndex:
                    pass
                elif firstNum + secondNum == target:
                    return [firstIndex, secondIndex]
