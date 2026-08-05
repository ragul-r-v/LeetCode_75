# 🚀 LeetCode 1768. Merge Strings Alternately

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Pattern](https://img.shields.io/badge/Pattern-Two%20Pointers%20%7C%20Simulation-orange)

## 📌 Problem information

| Category | Details |
|---|---|
| Problem number | 1768 |
| Difficulty | Easy |
| Topics | Strings, Two Pointers, Simulation |

## 📖 Problem statement

Create a new string by taking one character from `word1`, then one from `word2`. When either string is exhausted, append the remainder of the other string.

### Example

```text
word1 = "ab", word2 = "pqrs"
answer = "apbqrs"
```

## 💡 Intuition and pattern

This is a **two sequences traversal** problem: visit both strings at the same index until the shorter string ends, then append the leftover characters. Think of alternating cards from two decks.

## 🐍 Python concepts used

- `min()` finds the safe number of paired positions.
- String indexing reads a character at an index.
- `append()` adds one character to the result list.
- `extend()` adds every leftover character.
- `"".join(...)` efficiently creates the final string.

## 📝 Step-by-step algorithm

1. Set `n` to the length of the shorter string.
2. Create an empty `result` list.
3. For every index from `0` to `n - 1`, append the character from each word.
4. Extend the result with `word1[n:]` and `word2[n:]`.
5. Join and return the list.

```text
word1 and word2 → find min length → alternate characters
→ append leftovers → join → answer
```

## ✍️ Dry run

For `word1 = "abcd"` and `word2 = "pq"`:

| Step | Result |
|---|---|
| `i = 0` | `[a, p]` |
| `i = 1` | `[a, p, b, q]` |
| Append leftovers | `[a, p, b, q, c, d]` |
| Join | `"apbqcd"` |

## 💻 Python solution

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        n = min(len(word1), len(word2))

        for i in range(n):
            result.append(word1[i])
            result.append(word2[i])

        result.extend(word1[n:])
        result.extend(word2[n:])

        return "".join(result)
```

## ⏱ Complexity analysis

- Time: `O(m + n)` — every character is processed once.
- Space: `O(m + n)` — the result list holds every character.

## ❌ Common mistakes

- Using `max(...)` for the loop can access a missing index.
- Forgetting to append the leftover part of the longer word.
- Building the answer through repeated string concatenation instead of using a list and `join()`.

## 🎯 Quick revision

**Pattern:** Two sequences traversal. Stop at `min(len(word1), len(word2))`, then append the leftovers.

