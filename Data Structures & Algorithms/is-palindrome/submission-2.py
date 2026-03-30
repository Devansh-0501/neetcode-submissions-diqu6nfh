class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        n, l = 0, len(st) - 1

        while n < l:

            if not st[n].isalnum():
                n += 1

            elif not st[l].isalnum():
                l -= 1

            elif st[n] != st[l]:
                return False

            else:
                n += 1
                l -= 1

        return True
