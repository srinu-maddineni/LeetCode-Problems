class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k =Counter(nums)
        print(k)
        r = []
        for i in range(1,len(nums)+1):
            if k[i] == 0:
                r.append(i)
        return r

        
