class Solution:
         
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        rows, cols = len(text1)+1, len(text2)+1
        
        res = [ [0 for i in range(rows)] for j in range(cols)]
        
        for i in range(rows-2, -1, -1):
            for j in range(cols-2, -1, -1):
                res[j][i] = 1 + res[j+1][i+1] if text2[j]==text1[i] else max(res[j+1][i], res[j][i+1])
                
        
        return res[0][0]
    
          