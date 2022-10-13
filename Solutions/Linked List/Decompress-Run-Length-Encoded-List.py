class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # bruteforce
        n=[]
        for i in range(len(nums)-1):
            if i%2==0:
                for j in range(nums[i]):
                    n.append(nums[i+1])
        return n
