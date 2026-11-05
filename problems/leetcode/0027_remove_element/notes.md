# 0027 Remove Element

- **Link:** https://leetcode.com/problems/remove-element/
- **Difficulty:** Easy
- **Pattern:** Array, Two Pointers

## Key insight

I don't need to delete anything. Only the first `k` elements are checked, so I just
overwrite the front of the list with the elements I keep.

## Approach

Read every element in the list. When it isn't `val`, write it at index `k` and move
`k` forward by one. At the end, `k` is the number of kept elements.

## Complexity

- Time: O(n)
- Space: O(1)

## Trap

- I returned the number of removed elements instead of the number of kept ones.
- `nums = [...]` only points the local name at a new list, so the caller's list
  doesn't change. To change the list in place, assign into it, e.g. `nums[i] = ...`.
