class Solution:
    def search(self, nums: List[int], target: int) -> int:
       return self.binSearch(0, len(nums)-1, nums, target)
    
    def binSearch(self, left:int, right:int, nums: List[int], target: int) -> int:
        if left > right:
            return -1
        mid = left + (right - left) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binSearch(mid+1, right, nums, target)
        else:
            return self.binSearch(left, mid-1, nums, target)
        