class Solution:
    def compress(self, chars: List[str]) -> int:
        
        l,r  = 0,0
        pr = 0
        while r<len(chars):
           
            while r < len(chars)-1 and chars[r] == chars[r+1] :
                r +=1

            sl = r-l+1
            print(chars[l], ' ', r-l+1)
            fc = chars[l]
            r +=1
            l = r
           
            chars[pr] = fc
            pr +=1
            if sl > 1:
                sl = str(sl)
                for i in range(len(sl)):
                    chars[pr] = sl[i]
                    pr +=1
              

        return pr

        
        

