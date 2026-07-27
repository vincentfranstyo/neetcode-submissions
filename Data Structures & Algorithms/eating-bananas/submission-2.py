class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossibleRate(mid, h):
            count = 0
            for num in piles:
                count += math.ceil(num / mid)

            return count <= h

        lowest = 1
        highest = max(piles)
        piles = sorted(piles)
        mid = (lowest + highest) // 2
        
        while lowest <= highest:
            mid = (lowest + highest) // 2
            print(f'mid {mid}')
            if isPossibleRate(mid, h):
                highest = mid - 1
            else:
                lowest = mid + 1

        return lowest