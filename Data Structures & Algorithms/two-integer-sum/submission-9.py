class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        num_hash = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_hash:
                return [num_hash[diff], i]
            num_hash[nums[i]] = i
        