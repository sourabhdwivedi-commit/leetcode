class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[1]*n
        if n<=2:
            return 0
        prime[0]=prime[1]=0
        i=2
        while i*i<n:
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j]=0

            i+=1
        return sum(prime)

        