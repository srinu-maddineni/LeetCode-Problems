class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # print(type(knowledge))
        # stk = ''
        
        n = len(s)
        m = {}
        for i in range(len(knowledge)):
            m[knowledge[i][0]] = knowledge[i][1]
        res = []
        # print(s[1],m)
        i =0
        while i <n:
            if s[i] == '(':
                j=i+1
                while s[j] != ')':
                    j+=1
                res.append(m.get(s[i+1:j],'?'))
                i=j+1
            else:
                res.append(s[i])
                i+=1
        return ''.join(res)


