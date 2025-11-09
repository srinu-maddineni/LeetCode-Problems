class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        print(ord('A')-64)
        count = 0
        for i in range(len(columnTitle)):
                 count+=(ord(columnTitle[i])-64)+count*25
        return count


