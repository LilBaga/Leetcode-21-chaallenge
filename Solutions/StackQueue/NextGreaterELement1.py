class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    n = j
                    val = -1
                    while n < len(nums2):
                        if nums1[i] < nums2[n]:
                            val = nums2[n]
                            break
                        n+=1
                    res.append(val)                    
        return res
        # j=0
        # for i in range(reversed(len(nums2-1))):
        #     if nums2[i]>=nums2[res[j]]:
        #         result.append(nums2[i])
        #     else:
                
        # return result
