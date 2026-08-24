class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        st=list(s)
        slen=len(st)
        ta=list(t)
        i=0
        while st and ta:
            if st[0]==ta[0]:
                i+=1
                st.pop(0)
                ta.pop(0)
            else:
                ta.pop(0)
        return i==slen                   
