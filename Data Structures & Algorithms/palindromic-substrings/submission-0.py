class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expand(l,r):
            res = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        
        output = 0
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)
            output = output + odd + even
        
        return output

        