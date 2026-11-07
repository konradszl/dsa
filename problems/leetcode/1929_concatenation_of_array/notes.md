# 1929 Concatenation of Array

- **Link:** https://leetcode.com/problems/concatenation-of-array/
- **Difficulty:** Easy
- **Pattern:** Array

## Key insight

The result is twice as long as `nums`, and every element appears in it twice: once at
index `i` and once at index `i + len(nums)`.

## Approach

Create a list of length `2 * len(nums)`. Read every element once and write it to both
of its positions.

## Complexity

- Time: O(n)
- Space: O(n)

Big-O drops constant factors, so a result of size `2n` is still O(n).

## Trap

- I reused the file from 1299 and mixed up the names `arr` and `nums`.
