class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                
                stackTemp,stackIndex=stack.pop()
                res[stackIndex] = i - stackIndex

                
            
            stack.append([t,i])
        return res

        # i=0,t=30 stack=[[0,30]], i = 1,t=38 stack=[38,1] res=[1 0 0 0 0 0 0] 
        # i = 2, t=30 stack=[[38,1],[30,2]]
        # i = 3, t=36 stack=[[38,1]] res=[1 0 1 0 0 0 0]
        # i = 4, t=35 stack=[[38,1],[35,4]]
        # i = 5, t=40 stack= 
