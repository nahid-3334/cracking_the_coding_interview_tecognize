class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        end=len(nums)
        max=-1000000
        cs=0
        for i in range(end):
            cs+=nums[i]
            if cs>max:
                max=cs #
            if cs<0:#cs negative hole cs 0 theke start korbo
                cs=0      
        return max
    # TC-o(n);sc-O(1)

# def maxarray(nums):
#     end=len(nums)
    
#     for i in range(end):
#         s=0
#         for j in range(i,end):
#             s+=nums[j]
#             l.append(s)
#     return max(l)
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# print(maxarray(nums))        
# Complexity analysis

# Time complextiy : O(n2).

# Space complexity : O(n) 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        end=len(nums)
        max=-1000000
        for i in range(end):
            if nums[i]>max:
                max=nums[i]#store current max then compare with this
            currentsum=nums[i]
            for j in range(i+1,end):
                currentsum+=nums[j]
                if currentsum>max:
                    max=currentsum
        return max
    #TC-o(n2);sc-O(1)
