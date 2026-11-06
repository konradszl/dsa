# 0485 Max Consecutive Ones

- **Link:** https://leetcode.com/problems/max-consecutive-ones/
- **Difficulty:** Easy
- **Pattern:** Array, Running Count

## Key insight

I only need two numbers: `count`, the length of the current run, and `result`, the
longest run so far. A `0` ends the current run, so `count` can go back to zero.
Nothing is lost, because `result` already holds the best run.

## Approach

Read every element in the list. When the element is not `0`, increase `count` by one.
Otherwise, set `count` to zero. After each element, assign `max(result, count)` to
`result`. At the end, `result` is the length of the longest run of ones.

## Complexity

- Time: O(n)
- Space: O(1)

## Trap

- I used `max()` only to compare, in `if max(count, result) == count:`, then assigned
  in a second step. `max()` returns the value I want, so I can assign it directly.

## Python notes

- `if num` is more idiomatic than `if num != 0`.
- `result = max(result, count)` is more idiomatic than comparing with `>` and then
  assigning.
