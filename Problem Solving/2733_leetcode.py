class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if len(nums) <= 2:
            return -1
        else:
            return nums[1]