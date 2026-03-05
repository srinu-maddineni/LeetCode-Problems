class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        rel = 0
        for i in operations:
            if '+' in i:
                rel+=1
            else:
                rel-=1
        return rel
        
