class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end=len(nums)
        index=1 
        for i in range(1,end):
            if nums[i]!=nums[i-1]:# not match then assign element
                nums[index]=nums[i]
                index+=1
        return index        
# Complexity analysis

# Time complextiy : O(n). Assume that n is the length of array. Each of i and index traverses at most nn steps.

# Space complexity : O(1)