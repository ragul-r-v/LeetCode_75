# 🚀 LeetCode 1071. Greatest Common Divisor of Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Pattern](https://img.shields.io/badge/Pattern-Math%20%7C%20Strings-orange)

## 📌 Problem information

| Category | Details |
|---|---|
| Problem number | 1071 |
| Difficulty | Easy |
| Topics | Strings, Math |

## 📖 Problem statement

Find the largest non-empty string that can be repeated to form both `str1` and `str2`. If no common repeating block exists, return `""`.

For example, `"ABC"` divides both `"ABCABC"` and `"ABC"`.

## 💡 Key observation

If both strings are repetitions of the same base string, `str1 + str2` and `str2 + str1` are identical. If they differ, a common divisor string is impossible.

After that check, the length of the largest possible base is `gcd(len(str1), len(str2))`.

## 📝 Step-by-step algorithm

1. Compare `str1 + str2` with `str2 + str1`.
2. Return an empty string if they are not equal.
3. Find the GCD of the two lengths.
4. Return the prefix of `str1` with that length.

## ✍️ Dry run

```text
str1 = "ABABAB", str2 = "ABAB"

"ABABAB" + "ABAB" == "ABAB" + "ABABAB"  → True
gcd(6, 4) = 2
str1[:2] = "AB"
```

## 🐍 Python concepts used

- `+` concatenates strings.
- `math.gcd()` finds the greatest common divisor of two lengths.
- Slicing, `str1[:length]`, extracts the candidate prefix.

## 💻 Python solution

```python
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))
        return str1[:length]
```

## ⏱ Complexity analysis

- Time: `O(m + n)` — concatenation dominates the work.
- Space: `O(m + n)` — the concatenated strings require extra memory.

## ❌ Common mistakes

- Computing the GCD of the lengths without first checking the repeating pattern.
- Treating common characters or a common substring as a divisor string.
- Returning a prefix longer than the GCD length.

## 🎯 Pattern recognition and revision

When a problem contains repeated strings, shared blocks, or divisible lengths, consider **string concatenation plus GCD**.

**Key check:** `str1 + str2 == str2 + str1`  
**Answer:** `str1[:gcd(len(str1), len(str2))]`

