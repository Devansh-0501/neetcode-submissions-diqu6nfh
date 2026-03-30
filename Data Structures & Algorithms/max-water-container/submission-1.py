class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0

        n,l=0,len(heights)-1

        while n<l:
            length=l-n
            if heights[l]>heights[n]:
                breadth=heights[n]
                n+=1
            else:
                breadth=heights[l]
                l-=1
            area=length*breadth
            maxarea=max(maxarea,area)
        return maxarea
            

          
          


            
        