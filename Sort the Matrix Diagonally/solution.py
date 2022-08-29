class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        totalRows = len(mat)
        totalColumns = len(mat[0])
        column = 0
        row = 0
        
        while column < (totalColumns-1):
            self.sort(mat,0,column,totalRows,totalColumns)
            column += 1
        
        while row < (totalRows-1):
            self.sort(mat,row,0,totalRows,totalColumns)
            row += 1
            
        return mat
        
    def sort(self, mat: List[List[int]], masterrow, mastercolumn, totalRows, totalColumns):
        values = []
        row = masterrow
        column = mastercolumn
        while row<totalRows and column<totalColumns:
            values.append(mat[row][column])
            row += 1
            column += 1
        
        values.sort()
        row = masterrow
        column = mastercolumn
        index = 0
        while row<totalRows and column<totalColumns:
            mat[row][column] = values[index]
            index += 1
            row += 1
            column += 1
                
        