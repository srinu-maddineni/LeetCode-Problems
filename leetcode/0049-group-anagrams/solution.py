class Solution(object):
    def groupAnagrams(self, strs):
        ans = {}
        for c in strs:
            s_sorted = sorted(c)
            key = tuple(s_sorted)
            if key not in ans:
                ans[key] = [c]
            else:
                ans[key].append(c)
        return ans.values()

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
