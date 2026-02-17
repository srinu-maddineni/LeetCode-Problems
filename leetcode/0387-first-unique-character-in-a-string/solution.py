class Solution:
    def firstUniqChar(self, s: str) -> int:
        k = Counter(s)
        print(k)
        for i in k:
            if k[i] == 1:return s.find(i)
        return -1
