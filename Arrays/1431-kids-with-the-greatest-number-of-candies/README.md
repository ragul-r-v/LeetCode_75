# 🚀 LeetCode 1431. Kids With the Greatest Number of Candies

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Pattern](https://img.shields.io/badge/Pattern-Array%20Traversal-orange)

## 📌 Problem information

| Category | Details |
|---|---|
| Problem number | 1431 |
| Difficulty | Easy |
| Topics | Arrays |

## 📖 Problem statement

For each child, determine whether giving that child all `extraCandies` would let them have at least as many candies as the current greatest number. Return a Boolean result for every child.

```text
candies = [2, 3, 5, 1, 3], extraCandies = 3
answer = [True, True, True, False, True]
```

## 💡 Intuition

Every child is compared with the same value: the current maximum. Find it once, then check whether `candy + extraCandies >= maximum` for each child. The original array never needs to change.

This is the **precomputation + array traversal** pattern.

## ❌ Brute force vs. optimized approach

A brute-force solution could give candies to each child, repeatedly find the maximum, and undo the change. That is `O(n²)`.

The optimized solution computes `max(candies)` only once and traverses the list once, giving `O(n)` time.

## 📝 Step-by-step algorithm

1. Find `maximum = max(candies)`.
2. Create an empty answer list.
3. Visit every `candy` value.
4. Append `True` if `candy + extraCandies >= maximum`; otherwise append `False`.
5. Return the answer list.

## ✍️ Dry run

For `[2, 3, 5, 1, 3]` and `extraCandies = 3`, the maximum is `5`.

| Candies | After extra | Result |
|---:|---:|---|
| 2 | 5 | `True` |
| 3 | 6 | `True` |
| 5 | 8 | `True` |
| 1 | 4 | `False` |
| 3 | 6 | `True` |

## 🐍 Python concepts used

- `max()` obtains the greatest current candy count.
- A `for` loop visits every child.
- Boolean comparisons return `True` or `False`.
- A list stores the result for each child.

## 💻 Python solution

```python
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)

        answer = []

        for candy in candies:
            if candy + extraCandies >= maximum:
                answer.append(True)
            else:
                answer.append(False)

        return answer
```

## ⏱ Complexity analysis

- Time: `O(n)` — one pass to find the maximum and one to build the answer.
- Space: `O(n)` — one Boolean value is stored for each child.

## ❌ Common mistakes

- Calling `max(candies)` inside the loop.
- Using `>` instead of `>=`; tying the maximum is enough.
- Modifying the original array even though only a comparison is needed.

## 🎯 Quick revision

**Pattern:** Precomputation + array traversal. Compute the maximum once, then compare every possible total against it.
