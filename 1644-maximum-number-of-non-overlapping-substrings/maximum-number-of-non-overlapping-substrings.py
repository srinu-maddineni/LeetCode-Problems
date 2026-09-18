class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        m = {}
        for i,c in enumerate(s):
            if c not in m:
                m[c] = [i,i]
            else:
                m[c][1]=i
        # print(m)
        inter = []
        for ch,index in m.items():
            print(ch)
            f = index[0]
            l = index[1]+1
            i = f
            # a = 1
            valid = True
            while i<l:
                c = s[i]
                if f> m[c][0]:
                    valid = False
                    break
                l = max(l,m[c][1]+1)
                i+=1
            if valid:
                inter.append((f,l))
            
        inter.sort(key=lambda x:x[1])
        out = []
        e = -1
        for f,l in inter:
            if e<=f:
                out.append(s[f:l])
                e = l

        return out

        