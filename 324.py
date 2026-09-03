class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)
        
        small = nums[:(n + 1) // 2]
        large = nums[(n + 1) // 2:]
        
        small.reverse()
        large.reverse()
        
        for i in range(n):
            if i % 2 == 0:
                nums[i] = small[i // 2]
            else:
                nums[i] = large[i // 2]