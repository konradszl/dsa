# 0682 Baseball Game

- **Link:** https://leetcode.com/problems/baseball-game/
- **Difficulty:** Easy
- **Pattern:** Stack

## Key insight

Every operation only looks at the most recent valid scores, and `C` removes the most
recent one. "Last in, first out" is exactly what a stack does.

## Approach

Keep the valid scores in a list used as a stack. For each operation:

- `+`: push the sum of the last two scores.
- `D`: push double the last score.
- `C`: pop the last score.
- anything else: it's a number, so push `int(operation)`.

At the end, the answer is the sum of everything left on the stack.

## Complexity

- Time: O(n)
- Space: O(n)

## Trap

- I typed `operations` as `list[int]`, but the operations are strings. Python doesn't
  check type hints when the code runs, so the tests still passed.

## Python notes

- A plain `list` is Python's stack: `append()` pushes, `pop()` pops and `stack[-1]`
  peeks. There's no need for a separate `Stack` class like Java's `Deque`.
- `match`/`case` is Python's version of Java's `switch`, and `case _:` is the
  `default`.
- `int("-2")` parses negative numbers, so they need no special case.
