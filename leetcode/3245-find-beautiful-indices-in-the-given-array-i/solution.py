class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        if b not in s:
            return []
        n = len(s)
        print(n)
        a_l = len(a)
        b_l = len(b)
        arr = []
        for i in range(n-len(a)+1):
            a1 = s[i:a_l+i]
            if a1 == a:
                start = max(0, i - k)
                end = min(n - b_l, i + k)
                for j in range(start,end+1):
                    b1 = s[j:b_l+j]
                    if b1 == b:
                        if abs(j-i) <= k:
                            arr.append(i)
                            break
        print(arr)
        return arr
