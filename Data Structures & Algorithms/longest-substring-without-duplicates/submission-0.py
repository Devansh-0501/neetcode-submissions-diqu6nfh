class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        longest = 0
        seen={}

        while right < len(s):
            if s[right] in seen:
                left = max(left,seen[s[right]]+1)
            
            seen[s[right]]=right
            longest=max(longest,right-left+1)
            right+=1
        return longest
        #z:0,x:1,y:2,z:3