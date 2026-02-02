class Solution:
    def hammingWeight(self, n: int) -> int:
        # b = format(n,'032b')
        return bin(n).count('1')
        
