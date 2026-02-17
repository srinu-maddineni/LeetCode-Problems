class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = []
        for i in range(len(boxes)):
            k =0 
            for j in range(len(boxes)):
                if i == j:
                    continue
                else:
                    k += int(boxes[j])*abs(i-j)
            arr.append(k)
        return arr
        
