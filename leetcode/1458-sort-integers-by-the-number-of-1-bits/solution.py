class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ar = []
        for i in range(len(arr)):
            k = bin(arr[i])
            ar.append((k[2:].count("1"),arr[i]))
        ar.sort(key=lambda x:(x[0],x[1]))
        print(ar)
        return [x[1] for x in ar]

        
