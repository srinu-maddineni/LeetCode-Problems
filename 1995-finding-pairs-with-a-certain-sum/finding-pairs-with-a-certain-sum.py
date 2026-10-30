class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = Counter(nums2)
    def add(self, index: int, val: int) -> None:
        
        x = self.nums2[index]+val
        self.m[self.nums2[index]]-=1
        
        self.m[x]=(self.m[x]|0)+1
        self.nums2[index] = x


    def count(self, tot: int) -> int:
        res =0
        for i in range(len(self.nums1)):
            e = tot - self.nums1[i]
            if e in self.m:
                res+=self.m[e]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)