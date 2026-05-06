class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = {}
        for s in s1:
            s1dict[s] = s1dict.get(s, 0) + 1
        print(s1dict)
        s2dict = {}
        left = 0
        for right in range(len(s2)):
            s2dict[s2[right]] = s2dict.get(s2[right], 0) + 1
            if (right - left + 1) > len(s1):
                s2dict[s2[left]] -= 1
                if s2dict[s2[left]] == 0:
                    del s2dict[s2[left]]
                left += 1
            if s2dict == s1dict:
                return True
            print(s2dict)
        return False
            

