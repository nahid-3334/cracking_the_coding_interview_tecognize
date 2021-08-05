class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while (left <= right) :
            if target<nums[left] :#target <initial
                return left
            elif target>nums[right] :#target >end
                 return right+1  
            else:
                mid= int(left + (right - left) / 2)
            #Check if target is present at mid
                if (nums[mid] == target):
                    return mid
            #If target greater, ignore left half
                elif nums[mid] < target:
                     left = mid + 1
            #If target is smaller, ignore right half
                else:
                    right = mid - 1;
# Complexity analysis

# Time complextiy : O(logn). 

# Space complexity : O(1)