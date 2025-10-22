class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        n1 = num1[::-1]
        n2 = num2[::-1]

        pos1, pos2, rem  = 0,0,0
        res = []
        while pos1 < len(num1) and pos2 < len(num2):
            v = int(n1[pos1]) + int(n2[pos2])
            if v < 10:
                res.append(v + rem)
                rem = 0
            else:
                v1 = v // 10
                v2 = v % 10
                res.append(v2 + rem)
                rem = v1

            pos1 +=1
            pos2 +=1


        # print('res :',res)

        while pos1 < len(n1):
            v = int(n1[pos1])
            v += rem
            rem = 0

            if v < 10:
                res.append(v)
            else:
                v1 = v // 10
                v2 = v % 10
                res.append(v2)
                rem = v1

            pos1 +=1
           
    
        while pos2 < len(n2):
            v = int(n2[pos2])
            v += rem
            rem = 0
           
            if v < 10:
                res.append(v)
            else:
                v1 = v // 10
                v2 = v % 10
                res.append(v2)
                rem = v1

            pos2 +=1

        print('rem :',rem)

        if rem > 0:
            res.append(rem)

        res = res[::-1]
        res = list(map(str, res))
        res = ''.join(res)

        return res