class Solution:
    def bitwiseComplement(self, n: int) -> int:
        k = bin(n)[2:]
        s =''
        for i in k:
            if i =='1':
                s+='0'
            else:
                s+='1'
        return int(s,2)
