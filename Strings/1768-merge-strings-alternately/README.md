# 1768. Merge Strings Alternately

> **Difficulty:** Easy  
> **Pattern:** Two pointers / sequence traversal  
> **LeetCode:** [Problem link](https://leetcode.com/problems/merge-strings-alternately/)

## Problem overview

Combine two strings by taking one character from each in turn. If one string has characters left after the other ends, append them.

## Intuition

Each index can contribute at most one character from each word. Iterating through the longer word ensures no remaining character is missed.

## Approach

1. Create an empty list for the output.
2. Visit every index up to the longer word's length.
3. Append the character from each word only when that index exists.
4. Join the list into the answer string.

## Complexity

- Time: `O(m + n)`
- Space: `O(m + n)` for the result

## Key takeaway

When traversing two sequences of unequal length, guard each access with a bounds check.
