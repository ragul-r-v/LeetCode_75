from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Return the largest repeating base shared by both strings.

        Time: O(m + n)
        Space: O(m + n)
        """
        if str1 + str2 != str2 + str1:
            return ""

        return str1[:gcd(len(str1), len(str2))]
