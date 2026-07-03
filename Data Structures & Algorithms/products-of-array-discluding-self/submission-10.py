class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        have_zero = False
        prod = 1
        zero_ids = []
        for i, num in enumerate(nums):
            if num != 0:
                prod *= num
            else:
                have_zero = True
                zero_ids.append(i)
        
        res = []
        if len(zero_ids) > 1:
            return [0] * len(nums)

        if not have_zero:
            for num in nums:
                res.append(int(prod / num))
        else:
            res = [0] * len(nums)
            for zero_id in zero_ids:
                res[zero_id] = prod
        
        return res
