class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        m = {}
        for i in range(len(names)):
            m[heights[i]] = names[i]
        heights.sort(reverse=True)
        res = []
        print(m,heights)
        for i in range(len(names)):
            res.append(m[heights[i]])
        return res