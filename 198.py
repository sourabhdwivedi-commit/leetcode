class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b =0,0
        # here a is the max money we can  get upto i-1 houses
        # and b is upto i-2 houses
        for i in range(len(nums)):
            curr=max(a,b+nums[i])
            b=a
            a=curr       
        # at every iteration check if robbing the house gives us 
        # more money than skipping it. if it does then rob else skip 
        return a    