class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end=len(nums)
      
        for i in range(end):
            if nums[i]==target:# match return
                return i
            elif nums[i]>target:
                return  i
            elif i== end-1 :
                 return end
# Complexity analysis

# Time complextiy : O(n). 

# Space complexity : O(1)