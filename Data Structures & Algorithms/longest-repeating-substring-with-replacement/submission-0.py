class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fremap = {}
        result = 0
        left  = 0
        maxf = 0
        for right in range(len(s)):
            fremap[s[right]] = 1 + fremap.get(s[right], 0)
            maxf = max(maxf, fremap[s[right]])
            while (right-left+1) - maxf > k:
                fremap[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


    



        