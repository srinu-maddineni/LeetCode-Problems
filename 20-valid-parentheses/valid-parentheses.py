class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        m = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in range(len(s)):
            if len(stk) ==0 and s[i] in m:
                return False
            if s[i] in m and m[s[i]] != stk[-1]:
                return False
            elif s[i] in m and m[s[i]] == stk[-1]:
                stk.pop()
            else:
                stk.append(s[i])
        print(stk)
        return len(stk) ==0




        