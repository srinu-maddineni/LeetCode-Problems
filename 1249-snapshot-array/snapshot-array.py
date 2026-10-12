class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[(0,0)] for _ in range(length+1)]
        self.snapArr = []
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.snapId ,val))

    def snap(self) -> int:
        self.snapId+=1
        return self.snapId-1
        

    def get(self, index: int, snap_id: int) -> int:
        arr = self.array[index]
        ans = 0

        for i,v in arr:
            if i > snap_id:
                break
            ans = v
            
        return ans
             


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)