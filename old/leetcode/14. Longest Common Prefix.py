class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pos = 0
        is_equal = True

        while is_equal:

            ch = ''
            for i in range(len(strs)):

                if pos > len(strs[i])-1:
                    is_equal = False
                    break

                if i == 0:
                    ch = strs[i][pos]
                else:
                    if strs[i][pos] != ch:
                        is_equal = False
                        break
            
            if is_equal:
                pos +=1
            else:
                break
        
        return strs[0][:pos]
    


    class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

            
       
