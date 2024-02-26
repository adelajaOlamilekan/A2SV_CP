class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row_len = len(matrix)
        column_len = len(matrix[0])
        result = []
        
        for c in range(column_len):
            temp = []
            for r in range(row_len):
                temp.append(matrix[r][c])
            
            result.append(temp)

        return result