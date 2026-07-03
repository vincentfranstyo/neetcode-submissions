class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for i, num in enumerate(nums):
            if num != 0:
                prod *= num
            else:
                zero_count += 1
        
        res = [0] * len(nums)
        if zero_count > 1:
            return res

        if zero_count:
            for i, num in enumerate(nums):
                if num == 0:
                    res[i] = prod
                    
        else:
            for i, num in enumerate(nums):
                res[i] = prod // num
        
        return res
