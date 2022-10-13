class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Bruteforce solution
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[j]+nums[i]==target:
        #             return [i, j]

        # we can use dictionary to get O(n):
        # 1) data is ordered 
        # 2) a lot of search
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]]=i
            else:
                return [dic[target-nums[i]],i]
