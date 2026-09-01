class Solution:
    def myAtoi(self, s: str) -> int:
        ans=0
        sin=1
        i=0
        while i<len(s) and s[i]==' ':
            i+=1

        if i<len(s) and s[i] in '+-':
            if s[i]=='-':
                sin=-1

            i+=1    
    
        while i<len(s) and s[i].isdigit():
            ans=ans*10 +int(s[i])
            i+=1
        
        ans*=sin
        INT_MIN=-2**31
        INT_MAX=2**31 -1
        if ans<INT_MIN:
            return INT_MIN
        elif ans>INT_MAX:
            return INT_MAX    
        return ans             
