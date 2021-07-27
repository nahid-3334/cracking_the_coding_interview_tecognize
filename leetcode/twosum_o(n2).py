class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end=len(nums)
        for start in range(end):
            for j in range(start+1,end):
                sum=nums[start] + nums[j]
                if sum== target:
                    return [start , j]