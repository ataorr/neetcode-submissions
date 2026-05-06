class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        fremap = {}
        maxfre = 0
        left = 0
        for right in range(len(s)):

            fremap[s[right]] = fremap.get(s[right], 0) + 1
            maxfre = max(maxfre, fremap.get(s[right]))

            while (right - left + 1) - maxfre > k:
                fremap[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

            
        