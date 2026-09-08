class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,len(nums)-1
            while left<right:
                curr=nums[i]+nums[left]+nums[right]
                if abs(curr-target)<abs(best-target):
                    best=curr

                if curr<target:
                    left+=1
                elif curr>target:
                    right-=1
                else:
                    return curr    

        return best                    

        