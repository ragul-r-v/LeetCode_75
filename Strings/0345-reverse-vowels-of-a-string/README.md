# LeetCode 345. Reverse Vowels of a String

> **Difficulty:** Easy  
> **Pattern:** Two Pointers  
> **LeetCode:** https://leetcode.com/problems/reverse-vowels-of-a-string/

## Problem overview

Given a string `s`, reverse the order of its vowels while leaving every consonant and other character in its original position. Vowels are `a`, `e`, `i`, `o`, and `u`, in either lowercase or uppercase.

## Examples

```text
Input:  s = "IceCreAm"
Output: "AceCreIm"

Input:  s = "leetcode"
Output: "leotcede"
```

## Intuition

The first vowel must be exchanged with the last vowel, the second with the second-last, and so on. Two pointers can search inward from both ends to find the next pair of vowels to swap.

## Approach

1. Put all uppercase and lowercase vowels in a set for constant-time membership checks.
2. Convert the string to a list because strings are immutable in Python.
3. Move `left` rightward until it reaches a vowel, and move `right` leftward until it reaches a vowel.
4. Swap those vowels and continue inward until the pointers meet.
5. Join the character list into the final string.

## Python solution

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        left, right = 0, len(chars) - 1

        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1

            while left < right and chars[right] not in vowels:
                right -= 1

            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return "".join(chars)
```

## Complexity

- Time: `O(n)` — each pointer moves across the string at most once.
- Space: `O(n)` — the mutable character list stores the result.

## Key takeaway

When only selected characters need reversing, use two pointers to locate and swap those characters in place.
