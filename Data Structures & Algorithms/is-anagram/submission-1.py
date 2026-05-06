class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = {}
        for i in range(len(s)):
            c = s[i]
            if  c not in sdict:
                sdict[c] = 1
            else:
                sdict[c] += 1
        
        for i in range(len(t)):
            c = t[i]
            if  c not in sdict:
                return False
            else:
                sdict[c] -= 1
                if sdict[c] < 0:
                    return False
        
        return True