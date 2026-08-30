class Solution:           
    def integerReplacement(self, n: int) -> int:
        i=0
        while n!=1:
            if n%2==0:
                n=n/2
            else:
                if n==3:
                    n-=1
                elif n%4==1:
                    n-=1
                else:
                    n+=1        


            i+=1

        return i                    
        