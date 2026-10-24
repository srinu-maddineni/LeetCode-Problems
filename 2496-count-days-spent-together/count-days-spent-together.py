class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        m = [0]
        for i in month:
            m.append(m[-1]+i)
        print(m)
        day_a_a = m[int(arriveAlice[:2])-1] + int(arriveAlice[3:])
        day_a_l = m[int(leaveAlice[:2])-1] + int(leaveAlice[3:])

        day_b_a = m[int(arriveBob[:2])-1] + int(arriveBob[3:])
        day_b_l = m[int(leaveBob[:2])-1] + int(leaveBob[3:])

        a = 0
        if day_a_a <= day_b_a:
            a = day_b_a
        else:
            a = day_a_a
        
        b = 0
        if day_a_l<=day_b_l:
            b = day_a_l
        else:
            b = day_b_l
        print(a,b)
        if b < a:
            return 0
        print(a,b)
        return b-a+1

  