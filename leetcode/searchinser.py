class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
         left,right=0,len(nums)-1
         while (left <= right) {
           if target<nums[left] :
               return left
           elif target>nums[right] :
               return right+1  
            else:


        mid= left + (right - left) / 2
        #Check if target is present at mid
        if (arr[m] == )
            return m;
  
        // If x greater, ignore left half
        if (arr[m] < x)
            l = m + 1;
  
        // If x is smaller, ignore right half
        else
            r = m - 1;
    }
  
    // if we reach here, then element was
    // not present
    return -1;
# Complexity analysis

# Time complextiy : O(n). 

# Space complexity : O(1)

#linear search
# end=len(nums)

#         for i in range(end):
#             if nums[i]==target:# match return
#                 return i
#             elif nums[i]>target:
#                 return  i
#             elif i== end-1 :
#                  return end
# # Complexity analysis

# # Time complextiy : O(n). 

# # Space complexity : O(1) 