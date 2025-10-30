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
    

    lass Solution:
    def compress(self, chars: List[str]) -> int:
        
        ps = pw = 0
        ch_cnt = 0
        cur_char = chars[0]
        ps +=1
        ch_cnt +=1
        while ps < len(chars):

            if chars[ps-1] == chars[ps]:
                  ch_cnt +=1
            
            else:
                print(f'cur_char : {cur_char} ch_cnt {ch_cnt}')
            
                chars[pw] = cur_char 
                pw +=1
                
                if ch_cnt > 1:
                    for n in str(ch_cnt):
                        chars[pw] = n
                        pw +=1

                cur_char = chars[ps]
                ch_cnt = 1
            
            ps +=1
        
        print(f'cur_char : {cur_char} ch_cnt {ch_cnt}')
        
        chars[pw] = cur_char 
        pw +=1
                
        if ch_cnt > 1:
            for n in str(ch_cnt):
                chars[pw] = n
                pw +=1

        
        return pw
    
    

        
        

