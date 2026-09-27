class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        stk1 = []

        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stk1.append(len(stk))
                continue
            if s[i] == ')':
                j = stk1.pop()
                k = len(stk)
                stk = stk[:j]+stk[j:k][::-1]
            else:
                stk.append(s[i])
        return ''.join(stk)
