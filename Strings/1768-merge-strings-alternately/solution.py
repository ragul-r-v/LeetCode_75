class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Merge characters in alternating order.

        Time: O(m + n)
        Space: O(m + n)
        """
        merged = []
        longest = max(len(word1), len(word2))

        for index in range(longest):
            if index < len(word1):
                merged.append(word1[index])
            if index < len(word2):
                merged.append(word2[index])

        return "".join(merged)
