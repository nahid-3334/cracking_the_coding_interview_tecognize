class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end=len(nums)
        dict={}
        for i in range(end):
            if nums[i] in dict:
                return dict[nums[i]],i
            else:
                dict[target-nums[i]]=i #diff=target-nums[i]] key=diff,value -index of corresponding num
                
                
            