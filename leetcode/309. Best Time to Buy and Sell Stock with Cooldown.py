class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0

        income = 0
        posess = 0
        operation = ''
     

        for i in range(len(prices)):
            if i == 0:
                operation = 'b'
                posess +=1
                income -= prices[i]

            else:
                if operation == 's':
                    operation = 'c'
                else:
                    if prices[i-1] < prices[i]:
                        posess -=1
                        income += prices[i]
                        operation = 's'
                    else:
                        posess +=1
                        income -= prices[i]
                        operation = 'b'

        return income
