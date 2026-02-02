class Solution:
    def reverseBits(self, n: int) -> int:
        b = str(format(n,'032b'))[::-1]
        print(b)
        return int(b,2)
        
