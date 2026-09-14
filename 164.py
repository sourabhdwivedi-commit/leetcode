class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        gap=0
        nums.sort()
        for i in range(1,len(nums)):
            gap =max(gap,abs((nums[i-1]-nums[i])))
        return gap