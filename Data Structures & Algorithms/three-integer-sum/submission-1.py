class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                second, third = nums[left], nums[right]
                nsum = first+second+third
                if nsum == 0:
                    result.append([first, second, third])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nsum > 0:
                    right -= 1
                elif nsum < 1:
                    left += 1
        return result
            
            