class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans  = 0 
        arr = [False]*len(digits)
        s = set()

        def back(n):

            nonlocal ans
            if n>999:
                return
            if n>=100 and n%2 ==0 and n not in s:
                ans+=1
                s.add(n)
                return 
            if n>999:
                return 
            
            for i in range(len(digits)):
                if not arr[i]:
                    n=n*10 + digits[i]
                    arr[i] = not arr[i]
                    back(n)
                    n=n//10
                    arr[i] = not arr[i]
        back(0)
        return ans
