class Solution:
    def intToRoman(self, num: int) -> str:
        h ={
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M",
            4:"IV",
            9:"IX",
            40:"XL",
            90:"XC",
            400:"CD",
            900:"CM"
        }
        print(num//10)
        i = 0
        s=''
        while num:
            k = (num%10)* 10**i
            num = num//10
            
            if k in h:

                s = h[k]+s
            else:
                b = 10**i
                d = k//b
                if d<4:

                    s= (h[b]*d)+s
                else:
                    s=h[5*b]+(h[b]*(d-5))+s
            i+=1

        print(s)
        return s


        
