# 🚀 LeetCode 605. Can Place Flowers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Pattern](https://img.shields.io/badge/Pattern-Greedy%20%7C%20Array%20Traversal-orange)

## 📌 Problem information

| Category | Details |
|---|---|
| Problem number | 605 |
| Difficulty | Easy |
| Topics | Array, Greedy |

## 📖 Problem statement

The `flowerbed` array contains `0` for an empty plot and `1` for a plot that already has a flower. No two flowers may be adjacent. Determine whether `n` new flowers can be planted without breaking that rule.

```text
flowerbed = [1, 0, 0, 0, 1], n = 1
answer = True
```

## 💡 Intuition

An empty plot is safe only when both neighbouring plots are empty (or the plot is at an edge with no neighbour). Plant a flower as soon as a plot is safe; this greedy choice cannot reduce the number of flowers that can be placed later.

## 📝 Step-by-step algorithm

1. Return `True` immediately when `n` is `0`, because no new flowers are needed.
2. Visit every plot in the flowerbed.
3. Ignore plots that already contain a flower.
4. Check whether the left plot is empty or does not exist.
5. Check whether the right plot is empty or does not exist.
6. If both sides are safe, plant a flower and decrease `n`.
7. Return `True` as soon as `n` becomes zero; return `False` if the traversal ends first.

## ✍️ Dry run

For `flowerbed = [1, 0, 0, 0, 1]` and `n = 1`:

| Index | Plot | Neighbours empty? | Action | Remaining `n` |
|---:|---:|---|---|---:|
| 0 | 1 | — | Skip | 1 |
| 1 | 0 | No | Skip | 1 |
| 2 | 0 | Yes | Plant | 0 |

The answer is `True` immediately after planting at index `2`.

## 🐍 Python concepts used

- `range(len(flowerbed))` traverses the array by index.
- `or` handles edge positions without accessing outside the list.
- Updating `flowerbed[i]` records a newly planted flower for the following checks.

## 💻 Python solution

```python
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = i == 0 or flowerbed[i - 1] == 0
                right_empty = (
                    i == len(flowerbed) - 1
                    or flowerbed[i + 1] == 0
                )

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True

        return False
```

## ⏱ Complexity analysis

- Time: `O(n)` — each plot is examined at most once.
- Space: `O(1)` — the algorithm uses a few variables and modifies the input array in place.

## ❌ Common mistakes

- Accessing `flowerbed[i - 1]` or `flowerbed[i + 1]` without handling the first and last positions.
- Forgetting to update the flowerbed after planting, which could allow adjacent flowers.
- Returning `False` before checking every available plot.

## 🎯 Quick revision

**Pattern:** Greedy array traversal. For each empty plot, plant only when both neighbours are empty, then immediately update the array.
