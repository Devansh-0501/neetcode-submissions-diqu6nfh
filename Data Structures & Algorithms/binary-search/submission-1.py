class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1

        while start<=end:
            midIndex=(end+start)//2
            if nums[midIndex]<target:
                start=midIndex+1
            elif nums[midIndex]>target:
                end=midIndex-1
            else:
                return midIndex

        return -1