class Solution:
    def frequencySort(self, s: str) -> str:
        dit={}
            
        for i in s:
            if i not in dit:
                dit[i]=s.count(i)

        dit = dict(sorted(dit.items(), key=lambda x: x[1], reverse=True))
        s=""
        for k,v in dit.items():
            s+=k*v

        return s
        