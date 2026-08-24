class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        su=sum(nums)
        ans=0
        while su%k!=0:
            ans+=1
            su-=1

        return ans