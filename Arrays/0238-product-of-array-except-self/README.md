# LeetCode 238. Product of Array Except Self

> **Difficulty:** Medium
> **Pattern:** Prefix and suffix products
> **LeetCode:** https://leetcode.com/problems/product-of-array-except-self/

## Problem overview

For every position in `nums`, return the product of all values except the value at that position. The solution must run in linear time and cannot use division.

## Examples

```text
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Input:  nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

## Intuition

The answer for an index is the product of everything before it multiplied by the product of everything after it. Build the left products in the output array, then make a reverse pass that multiplies in the right products.

This naturally handles zeroes without any special-case logic.

## Approach

1. Create `answer`, filled with `1`.
2. Traverse left to right. Store the product of all previous values at each index.
3. Traverse right to left. Multiply each stored prefix product by the product of all following values.
4. Return `answer`.

## Dry run

For `nums = [1, 2, 3, 4]`, the forward pass produces prefix products `[1, 1, 2, 6]`.

| Index | Right product before index | Final answer |
|---:|---:|---:|
| 3 | 1 | 6 |
| 2 | 4 | 8 |
| 1 | 12 | 12 |
| 0 | 24 | 24 |

## Python solution

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)

        left_product = 1
        for i in range(len(nums)):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
```

## Complexity

- Time: `O(n)` - two passes over the input.
- Space: `O(1)` extra space - the output array is required and only two product variables are used.

## Key takeaway

When division is unavailable, combine a prefix product with a suffix product to exclude the current element in linear time.
