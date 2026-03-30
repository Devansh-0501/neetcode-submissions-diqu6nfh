class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n,l=0,len(numbers)-1

        while(n<l):
            if numbers[n]+numbers[l] == target:
                return [n+1,l+1]
            elif numbers[n]+numbers[l] < target:
                n+=1
            else:
                l-=1
     