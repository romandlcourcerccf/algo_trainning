class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2
            hours = sum([math.ceil(p / k)  for p in piles])
            if hours <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k+1
        
        return res


/////////////////////

lass Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        print(piles)

        ks = [i for i in range(min(piles), max(piles)+1)]
        
        print(ks)

        l,r = 0, len(ks)-1
        while l <= r:
            k = (l+r) // 2
            print('k', k, 'ks[k]', ks[k])
            hours = [math.ceil(p / ks[k])  for p in piles]
            print(hours)
            hours_total = sum(hours)
            print('hours_total :', hours_total)
            if hours_total == h:
                return ks[k]
            elif hours_total < h:
                r = k-1
            else:
                l = k+1

        return -1