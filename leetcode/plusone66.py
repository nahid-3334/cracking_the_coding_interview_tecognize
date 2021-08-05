class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        end=len(digits)-1
        num=1
        while end>=0:
            last=digits[end]
            digits[end]=(last+num)%10
            num= int((last+num)/10)
            end-=1
        if digits[end+1]==0:
            digits.insert(0,1)
        return digits
                    total-=1
# Complexity analysis

# Time complextiy : O(n).

# Space complexity : O(1)