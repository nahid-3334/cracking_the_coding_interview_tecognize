class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #nums2 add to nums1 bu compaeing in sorted form ;if m==n only add nums2
        total=m+n-1
        end1=m-1
        end2=n-1
        while end2>=0:
            if end1>=0 and nums2[end2]<nums1[end1]:
                nums1[total]=nums1[end1]
                end1-=1
            else:
                nums1[total]=nums2[end2]
                end2-=1

    
# Complexity analysis

# Time complextiy : O(n).

# Space complexity : O(1)