# 1071. Greatest Common Divisor of Strings

> **Difficulty:** Easy  
> **Pattern:** Math + strings  
> **LeetCode:** [Problem link](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

## Problem overview

Find the longest non-empty string that can be repeated to form both input strings.

## Intuition

Two strings share a repeating base exactly when concatenating them in either order gives the same result. The base length is the greatest common divisor of their lengths.

## Approach

1. Check whether `str1 + str2` equals `str2 + str1`.
2. If not, no common divisor string exists.
3. Otherwise, return the prefix whose length is `gcd(len(str1), len(str2))`.

## Complexity

- Time: `O(m + n)`
- Space: `O(m + n)` because of concatenation

## Key takeaway

For repeating-string problems, divisibility of lengths and equality under swapped concatenation reveal the shared pattern.
