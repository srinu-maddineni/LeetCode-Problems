class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        if len(colors)<3:
            return 0
        colors.insert(0,colors[-1])
        colors.append(colors[1])
        c =0
        for i in range(2,len(colors)):
            if colors[i] == colors[i-2] and colors[i] != colors[i-1] and colors[i-1] != colors[i-2]:
                c+=1
        return c

        
