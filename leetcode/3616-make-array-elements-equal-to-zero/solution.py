class Solution(object):
    def countValidSelections(self, nums):
        count = 0
        n = len(nums)
        for i in range(n):
            right = 0
            left = 0
            print(right,left,sum(nums[i+1:n]),sum(nums[0:i]))
            if nums[i] == 0:
                right = sum(nums[i+1:n])
                left = sum(nums[0:i])
                
                if right == left:
                    count+=2
                elif right-1==left:
                    count+=1
                elif right == left-1:
                    count+=1
                print(count)
        return count


        """
        :type nums: List[int]
        :rtype: int
        """
        
