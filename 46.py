class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(i,path):
            if i==len(nums):
                result.append(path[:])
                return

            for j in range(len(nums)):
                if nums[j] not in path:
                    path.append(nums[j])
                    backtrack(i+1,path)
                    path.pop()

        backtrack(0,[])
        return result                

