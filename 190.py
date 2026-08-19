class Solution:
    def reverseBits(self, n: int) -> int:
        binary=bin(n)[2:].zfill(32)
        binary=str(binary)[::-1]
        return int(binary,2)
        