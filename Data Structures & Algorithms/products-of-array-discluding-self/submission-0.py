class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_sum  =1
        zero_cnt = 0
        for n in nums:
            if n == 0:
                zero_cnt += 1
                continue
            total_sum *= n
        if zero_cnt >= 2:
            return [0] * len(nums)
        result = []
        for n in nums:
            if zero_cnt == 1:
                if n == 0:
                    result.append(total_sum)
                else:    
                    result.append(0)
            elif n == 0:
                result.append(0)
            else:
                result.append(total_sum // n)
        return result