class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]

        print("num1: ", num1, "num2: ", num2)

        res = []
        rem = i1 = i2 = 0
        while i1 < len(num1) and i2 < len(num2):
            s = int(num1[i1]) + int(num2[i2]) + rem
            rem = 0

            if s > 9:
                d, r = divmod(s, 10)
                res.append(str(r))
                rem = d
            else:
                res.append(str(s))

            i1 += 1
            i2 += 1

            print("res :", res)

        if i1 < len(num1):
            while i1 < len(num1):
                s = int(num1[i1]) + rem
                rem = 0

                if s > 9:
                    d, r = divmod(s, 10)
                    res.append(str(d))
                    rem = r
                else:
                    res.append(str(s))

                i1 += 1

        if i2 < len(num2):
            while i2 < len(num2):
                s = int(num2[i2]) + rem
                rem = 0

                if s > 9:
                    d, r = divmod(s, 10)
                    res.append(str(d))
                    rem = r
                else:
                    res.append(str(s))

                i2 += 1

        if rem > 0:
            res.append(str(rem))

        print(res)

        return "".join(res[::-1])
