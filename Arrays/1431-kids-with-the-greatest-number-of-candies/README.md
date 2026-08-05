# 1431. Kids With the Greatest Number of Candies

> **Difficulty:** Easy  
> **Pattern:** Precomputation + traversal  
> **LeetCode:** [Problem link](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

## Problem overview

For each child, decide whether receiving all extra candies would let them tie or exceed the current highest count.

## Intuition

The comparison point is the same for every child: the largest number already in the list. Compute it once instead of repeatedly comparing every pair.

## Approach

1. Find the current maximum candy count.
2. For each child, add `extraCandies`.
3. Record whether that total is at least the maximum.

## Complexity

- Time: `O(n)`
- Space: `O(n)` for the boolean result list

## Key takeaway

Precompute a shared value once when every element needs to be compared against it.
