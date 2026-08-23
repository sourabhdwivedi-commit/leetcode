class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rc=nums.count(0)
        wc=nums.count(1)
        bc=nums.count(2)
        for i in range(rc):
            nums[i]=0
        for i in range(rc,wc+rc):
            nums[i]=1
        for i in range(rc+wc,len(nums)):
            nums[i]=2           


                     
        
        