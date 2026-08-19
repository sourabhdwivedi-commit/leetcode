class Solution:
    def reverseBits(self, n: int) -> int:
        # bin(n)-> converts a num to its binary eqivalent
        # [2:] removes starting two chars which are 0b which python adds itself for binary nums
        # .zfill(32) fills the left side till 32 limit is reached. the solution requires it
        binary=bin(n)[2:].zfill(32)
        # reverse the binary by converting it to string using string slicing [::-1] -> reverses string
        binary=str(binary)[::-1]
        # int(x,y) converts a string x to integer with base y 
        return int(binary,2)
        
