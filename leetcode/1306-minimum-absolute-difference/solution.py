class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        # print(arr)
        min_diff =float(inf)
        for i in range(1,len(arr)):
            if arr[i]- arr[i-1] < min_diff:
                min_diff = arr[i]- arr[i-1]
        k =[]
        for i in range(1,len(arr)):
            if arr[i]- arr[i-1] == min_diff:
                k.append([arr[i-1],arr[i]])
        print(k)
        return k

        
