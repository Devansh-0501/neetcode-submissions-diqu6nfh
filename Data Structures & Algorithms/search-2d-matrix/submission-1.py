class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start,end=0,len(matrix)-1

        while start<=end:
            midIndex=(start+end)//2
           
            if matrix[midIndex][0] == target:
                return True
            elif matrix[midIndex][0]<target:
                start=midIndex+1
            else:
                end=midIndex-1

        start1,end1=0,len(matrix[end])-1
        while start1<=end1:
            midIndex1=(start1+end1)//2

            if matrix[end][midIndex1] == target:
                return True
            elif matrix[end][midIndex1] < target:
                start1=midIndex1+1
            else :
                end1=midIndex1-1
        return False
        