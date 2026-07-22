class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) time, O(1) space
        nums = sorted(nums)
        res = set()

        for i in range(len(nums)):
            remainder = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == remainder:
                    # print(f"appending [{nums[i]}, {nums[left]}, {[nums[right]]}")   
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < remainder:
                    left += 1
                    # print("moving left")
                elif nums[left] + nums[right] > remainder:
                    right -= 1
                    # print("moving right")
        
        return [s for s in res]
