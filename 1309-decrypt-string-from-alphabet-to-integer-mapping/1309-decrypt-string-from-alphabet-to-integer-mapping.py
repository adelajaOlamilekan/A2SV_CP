class Solution:
    def freqAlphabets(self, s: str) -> str:
        offset = 96
        output = ""
        temp = ""
        met_hash = 0
        
        for i in range (len(s)-1, -1, -1):
            
            if met_hash:
                met_hash -= 1
                continue
                
            if s[i] == "#":
                met_hash = 2
                temp = s[i-2 : i]
                temp = int(temp) + offset
            else:
                temp = int(s[i]) + offset
                
            output = chr(temp) + output
            
        return output
                