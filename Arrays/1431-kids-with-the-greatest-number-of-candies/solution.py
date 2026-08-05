from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """Determine which children can reach the current maximum.

        Time: O(n)
        Space: O(n) for the answer
        """
        current_maximum = max(candies)
        return [candy + extraCandies >= current_maximum for candy in candies]
