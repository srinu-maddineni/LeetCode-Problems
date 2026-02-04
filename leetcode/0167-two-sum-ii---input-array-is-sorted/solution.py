class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers)-1
        h = {}
        while i < j:
            c = numbers[i]+numbers[j]
            if c == target:
                return [i+1,j+1]
            elif c < target:
                i+=1
            elif c > target:
                j-=1
        

        
