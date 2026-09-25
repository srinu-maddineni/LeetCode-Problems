class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        # if n ==1 and k==1:
        #     return [1]
        # ans = []
        # nums.sort()
        # i =0
        # j=i+1
        # while i<n and j<n:
        #     print(j)
        #     if nums[i] != nums[j]:
        #         r = j-i
        #         if r>=k:
        #             ans.append(nums[i])
        #         i=j
        #         j=i+1
        #     else:
        #         j+=1
        # return ans



        m = {}
        ans = []
        for i in range(n):
            if not m.get(nums[i]):
                m[nums[i]] =0
            m[nums[i]] = m.get(nums[i])+1
        r=0
        for i,j in m.items():
            ans.append([i,j])

        # print(ans)
        ans.sort(key=lambda x:x[1],reverse=True)
        # print(ans)
        res = []
        for i in ans:
            if r>=k:
                break
            res.append(i[0])
            r+=1

        return res