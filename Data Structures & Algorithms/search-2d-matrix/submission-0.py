class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mid = top+(bot-top)//2
            l = len(matrix[mid]) - 1
            if matrix[mid][0] <= target <=matrix[mid][l]:
                return self.binSearch(matrix[mid], 0, l, target)
            if matrix[mid][l] < target:
                top = mid+1
            else:
                bot = mid-1
        return False

    def binSearch(self, nums, left, right, target) -> bool:
        if left > right:
            return False
        mid = left + (right-left) //2
        if nums[mid] == target:
            return True
        if nums[mid] < target:
            return self.binSearch(nums,mid+1,right,target)
        return self.binSearch(nums,left,mid-1,target)