class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax = 0
        leftMin =  0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            
            if c == ")":
                leftMin -= 1
                leftMax -= 1
            
            if c == "*":
                leftMin -= 1
                leftMax += 1
            
            if leftMax < 0:
                return False
            
            leftMin = max(0,leftMin)

        return leftMin == 0

        