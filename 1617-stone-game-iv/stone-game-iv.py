class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # def perfect(a):
        #     r = math.floor(a **(0.5))
        #     if r*r == a:
        #         return True
        #     else: return False
        memo = {}
        def help(num):
            if num==0: return False
            if num in memo : return memo[num]
            i = 1
            while i*i <= num:
                result = num - i*i
                    
                
                if not help(result):
                    memo[num] = True
                    return True
                i+=1
            memo[num] = False
            return False
        return help(n)

        