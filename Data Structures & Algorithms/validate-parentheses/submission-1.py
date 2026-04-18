class Solution:
    def isValid(self, s: str) -> bool:
        if s is None: return False
        prev = None

        while prev != s:
            prev = s
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        
        return s == ""
        