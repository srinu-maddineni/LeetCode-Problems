class MyHashSet(object):

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]
    
    def hash(self,key):
        return key%self.size
        

    def add(self, key):
        index = self.hash(key)
        if key not in self.bucket[index]:
            self.bucket[index].append(key)

        """
        :type key: int
        :rtype: None
        """
        

    def remove(self, key):
        index = self.hash(key)
        if key in self.bucket[index]:
            self.bucket[index].remove(key)

        """
        :type key: int
        :rtype: None
        """
        

    def contains(self, key):
        index = self.hash(key)
        return key in self.bucket[index]
        """
        :type key: int
        :rtype: bool
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
