class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stk = []
        st = []
        for i in range(1,n+2):
            if stk == target:
                return st
            if not stk:
                st.append("Push")
                stk.append(i)
            else:
                if stk[-1] not in target:
                    st.append("Pop")
                    stk.pop()
                    stk.append(i)
                    st.append("Push")
                else:
                    st.append("Push")
                    stk.append(i)
                
            print(stk)
        return st
        

        
