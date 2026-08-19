class Solution:
    def hammingWeight(self, n: int) -> int:
        # bin(n)-> given binary equivalent of a number
        # .count("1")-> counts the occurences 
        return bin(n).count("1")