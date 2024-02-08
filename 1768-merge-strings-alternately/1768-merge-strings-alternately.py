class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        
        len_str = 0
        
        if len(word1) <= len(word2):
            len_str = len(word1)
            
            for i in range(len_str):
                result += word1[i] + word2[i] 
            
            result += word2[len_str:len(word2)]
            
        else:
            len_str = len(word2)
            
            for i in range(len_str):
                result += word1[i] + word2[i] 
            
            result += word1[len_str:len(word1)]
        
        return result
        
        