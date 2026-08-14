# LeetCode 151. Reverse Words in a String

> **Difficulty:** Medium
> **Pattern:** String parsing
> **LeetCode:** https://leetcode.com/problems/reverse-words-in-a-string/

## Problem overview

Reverse the order of the words in `s`. A word is any consecutive sequence of non-space characters. The returned string must contain exactly one space between words, with no leading or trailing spaces.

## Examples

```text
Input:  s = "the sky is blue"
Output: "blue is sky the"

Input:  s = "  hello world  "
Output: "world hello"
```

## Intuition

Python's `split()` without an argument already handles the whitespace rules: it removes leading and trailing spaces and treats consecutive spaces as one separator. Once the words are extracted, reverse them and join them with a single space.

## Approach

1. Call `s.split()` to create a list of words.
2. Reverse the list with slicing, `[::-1]`.
3. Join the reversed words using one space.

## Python solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
```

## Complexity

- Time: `O(n)` - each character is processed while splitting and joining.
- Space: `O(n)` - the word list and returned string store the input characters.

## Key takeaway

For whitespace-normalization tasks in Python, `split()` followed by `" ".join(...)` is concise and correctly removes extra spaces.
