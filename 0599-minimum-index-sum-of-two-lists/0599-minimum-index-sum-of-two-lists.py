class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sum = 0
        result = {}
        
        for index1, word in enumerate(list1):
            if word in list2:
                index2 = list2.index(word)
                sum = index1+index2
                if sum in result:
                    result[sum].append(word)
                else:
                    result[sum] = [word]
        
        min_index = min(result.keys())
        
        return result[min_index]
                
                
        