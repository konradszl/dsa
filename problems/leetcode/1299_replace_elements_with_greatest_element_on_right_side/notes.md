# 1299 Replace Elements with Greatest Element on Right Side

- **Link:** https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
- **Difficulty:** Easy
- **Pattern:** Array, Reverse Traversal

## Key insight

Going from left to right, every element has to scan everything after it again. Going
from right to left, I already know the greatest element to the right, so one number,
`right_max`, replaces the inner loop.

## Approach

Start with `right_max = -1`, because the last element has nothing to its right. Walk
the list backwards. Save `max(right_max, arr[i])` in `new_max` before overwriting
`arr[i]` with `right_max`, then set `right_max` to `new_max`. The order matters: the
current element must not count as being on its own right side.

## Complexity

- Time: O(n)
- Space: O(1)

## Trap

- My first version used nested loops, which is O(n^2). It worked, but it repeated the
  same scan for every element. I needed a hint to see that going backwards removes
  the inner loop.
- I had trouble with the backwards `range`. The stop value is excluded, so reaching
  index 0 needs a stop of `-1`: `range(len(arr) - 1, -1, -1)`.

## Python notes

- `range(start, stop, step)` includes `start` and excludes `stop`.
- My first version named a variable `max`, which hides the built-in `max()`.