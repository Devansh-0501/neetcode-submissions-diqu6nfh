# "A A B B A B" k=2
#

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right=0,0
        seen={}
        res=0

        while right<len(s):
        
            seen[s[right]]=seen.get(s[right],0)+1

            if (right-left+1) - max(seen.values()) > k:
                seen[s[left]]-=1
                left+=1

            res=max(right-left+1,res)
            right+=1
        return res
            
            

        
        