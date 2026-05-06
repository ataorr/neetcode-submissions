class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        streak = 1
        result = 0
        for n in nums:
            if (n-1) not in numset:
                temp = n
                while (temp+1) in numset:
                    streak += 1
                    temp += 1
            result = max(result, streak)
            streak = 1
        return result
        
