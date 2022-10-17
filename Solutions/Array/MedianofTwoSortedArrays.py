class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        n = sorted(n)
        if len(n) % 2 == 0:
            res =  (n[(len(n)//2)-1] +  n[len(n)//2] )/ 2
        else:
            res =  n[len(n)//2]
        return res
