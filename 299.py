class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull,cow=0,0
        secret=list(str(secret))
        guess=list(str(guess))
        i=0
        while i<len(secret):
            if secret[i]==guess[i]:
                bull+=1
                secret.pop(i)
                guess.pop(i)
                continue
            
            i+=1

        i=0
        while i<len(secret):
            if secret[i] in guess:
                cow+=1
                guess.remove(secret[i])    

            i+=1        
              
        return str(bull)+'A'+str(cow)+'B'            
        