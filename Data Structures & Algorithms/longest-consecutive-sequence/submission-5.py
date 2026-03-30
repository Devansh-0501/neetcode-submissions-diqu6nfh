class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        temp=sorted(set(nums))
        print(temp)
        count=0
        longest=0
        for i in range(len(temp)-1):
            if temp[i+1]-temp[i]==1:
                count+=1
            else:
                longest=max(longest,count)
                count=0
        return max(longest,count)+1