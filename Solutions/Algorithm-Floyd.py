class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 18 tests
        # if sum(set(nums)) < len(nums):
        #     return sum(set(nums))
        # total = sum(nums) #12
        # full = sum(set(nums))+len(nums)
        # return len(nums)-(full - total)
        # 53 tests
        # for i in nums:
        #     total = nums.count(i)
        #     if total >1:
        #         return i
        ptr1 = nums[0]
        ptr2 = nums[0]
        while nums:
            ptr1 = nums[ptr1]
            ptr2 = nums[nums[ptr2]]
            if(ptr1 == ptr2 ):
                break
        ptr1 = nums[0]
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
                
