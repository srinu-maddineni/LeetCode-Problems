class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        ar = [float('inf')]*10
        for i in str(n):
            if ar[int(i)] == float('inf'):
                ar[int(i)] = 0
            ar[int(i)]+=1
        val = 0
        m = float('inf')
        for i in range(10):
            if ar[i]<m:
                m = ar[i]
                val = i
        return val