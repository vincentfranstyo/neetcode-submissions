class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]

        # hashmap
        num_map = defaultdict(int)
        for i, num in enumerate(numbers):
            diff = target - num
            if num in num_map:
                return [num_map[num], i + 1]
            num_map[diff] = i + 1

