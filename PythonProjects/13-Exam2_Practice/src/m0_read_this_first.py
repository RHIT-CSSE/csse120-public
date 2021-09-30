"""
The practice problems in m1_exam2_practice let you practice all the
patterns you have seen regarding sequences.  For each problem, FIRST
decide which PATTERN(S) are appropriate to the problem,
then apply the ideas as needed to the particular problem.

There is one problem that requires a version of the "find-best" pattern
that you have NOT yet seen.  It differs from all previous find-best problems
that you have done in the following respect:

    Previously, you could always start the "best found so far" as the item
    at index 0 of the sequence.  You then loop through the remaining items,
    comparing each to the "best found so far", and updating the
    "best found so far" whenever you find a new "best" one.

    In   practice1h   of m1_exam2_practice, the loop works the same way.
    However, you CANNOT start the "best found so far" as the item at
    index 0, because (in this problem) the item at index 0 is not guaranteed
    to be a candidate for "best".  (See the problem for details.)

    One solution is to write a PRELIMINARY loop that looks for
    a CANDIDATE "best".  If no candidate exists, then return the value
    that the problem asks you to return in that case.  But if a candidate
    exists, you can set the "best found so far" to that candidate, and then
    continue into the 2nd loop as with the previous "find best" problems.

    Get help from your instructor or student assistants
    if you get to   practice1h   and this does not make sense to you.
"""