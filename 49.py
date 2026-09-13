class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        dit={}
        for st in strs:
            if ''.join(sorted(st)) in  dit:
                dit[''.join(sorted(st))].append(st)
            else:
                dit[''.join(sorted(st))]=[st]

        for k,v in dit.items():
            ans.append(v)

        return ans            
