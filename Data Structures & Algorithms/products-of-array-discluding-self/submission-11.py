class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for i, num in enumerate(nums):
            if num != 0:
                prod *= num
            else:
                zero_count += 1
        
        res = []
        if zero_count > 1:
            return [0] * len(nums)

        if zero_count:
            for num in nums:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(int(prod / num))
        
        return res
