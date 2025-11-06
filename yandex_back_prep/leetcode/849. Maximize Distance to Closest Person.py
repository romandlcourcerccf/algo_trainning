class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        max_zeros_len = float('-inf')
        max_lef = -1
        max_right = -1

        l, r = 0, 0
        
        while l < len(seats) and r < len(seats):
            if seats[r] == 1:
                if r-l > max_zeros_len:
                    max_zeros_len = r-l
                    max_lef = l
                    max_right = r-1
                r +=1
                l =r
            elif r < len(seats):
                r +=1
        
        if r-l > max_zeros_len:
            max_zeros_len = r-l
            max_lef = l
            max_right = r

        print('max_zeros_len :', max_zeros_len)
        print('max_lef :', max_lef)
        print('max_right :', max_right)

        if not (max_lef == 0 or max_right == len(seats)-1) and  (max_right + max_lef) % 2 == 0:
            print('l-r :', max_right-max_lef)
            mid = (max_right + max_lef) // 2
            return max(mid - max_lef+1, max_right - mid+1)
        elif not (max_lef == 0 or max_right == len(seats)-1) and  (max_right + max_lef) % 2 != 0:
            print('l-r :', max_right-max_lef)
            mid = (max_right + max_lef) // 2
            return max(mid - max_lef, max_right - mid)
        if max_lef == 0 and max_right > 0:
            return max_right+1
        elif max_right == 0:
            return max_lef+1
        else:
            return r-l // 2
            




