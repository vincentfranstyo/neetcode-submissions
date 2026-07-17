class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0


        values = set(nums)
        longest = 0

        for num in values:
            if num - 1 in values:
                current = num
                length = 1

                while current + 1 in values:
                    length += 1
                    current += 1
                
                longest = max(longest, length + 1)
        
        return longest if longest > 0 else 1