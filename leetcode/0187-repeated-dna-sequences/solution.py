class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <10:
            return []
        # seen = {}
        # for i in range(len(s)-9):
        #     s1 = s[i:i+10]
        #     if s1 in seen:
        #         seen[s1] +=1
        #     else:
        #         seen[s1] = 1
        # rel = []
        # for i in seen:
        #     if seen[i] >1:
        #         rel.append(i)
        # return rel
        seen,rel =set(),set()
        for i in range(len(s)-9):
            s1 = s[i:i+10]
            if s1 in seen:
                rel.add(s1)
            seen.add(s1)
        return list(rel)
        
