Workflow
========

Continues branches
------------------
There are three continues branches; `main`, `test` and `live`.

`main` is the main development branch, finished feature branches and fixes get
merged into this one.

`test` is a Quality Assurance and Release Management branch, it get's manually
branched off from `main`. Once the `test` branch is approved the changes get
deployed into `live` via an automatic process.

`live` is a branch that is used for deploy, it gets update via a squashed
commit from `test`. The commit message will become the release notes.


Multiple Supported Versions
---------------------------
If multiple versions need to be supported, simultaneously each version will have
their own repository, forked from the original one.


Ephemeral branches
------------------
These branches are deleted once they are merged in, they consist of branches
that are prefixed as followed.

- `fix-` branches that contain fixes or updates but do not change the intended 
functionality.
- `new-` branches that contain new functionality, this can be brand new or
additional functionality.

All ephemeral branches must have a ticket associated with them,
so for example if a ticket 123 is there that solves an error when inserting a
specific records the branch name would be like this:

`fix-123-error-inserting-record`

Ephemeral branches require at least 1 review and passing of the automated
checks to be merged. The person who created the ephemeral branch does the
merging in (so not the reviewer).

The reviewer should always approve a merge request unless the reviewer sees
potential functional problems, these problems are **not**:
 - it is not working (the unit tests should confirm it is working).
 - it is not up to coding convention (the linter should detect this).
 - it is using an older dependency (the package version checker should detect
   this).

These may however be:
 - there are insufficient tests (thus doesn't detect it isn't working).
 - the functionality is a duplication and should be refactored.
 - the implementation is convoluted, thus requires either comments or perhaps
   a different way to implement it that doesn't require comments (give example
   in the change request).
   
If there is a dispute between author and reviewer that can not be solved among
them, then this should be mentioned in the organisations instant messaging 
communication channel (i.e. `DevOps`), where most likely a healthy discussion
will take place and the decision based on majority preference should be
followed by the reviewer and the author.

If there is still a dispute, a tie breaker will follow, this is in the form of
all disputing parties propose a fully functional PR using the same unit tests,
the different PR's will be judged on the following, in order:
 - Descriptive names of function, variables and namespaces (e.g. classes,
    modules)
 - Lowest amount of 'magic', e.g. effects that happen buried down, for example;
    an attribute gets renamed by a class inherited way down that hooks into the
    class constructor to change attribute names.
 - Lowest amount of processing time.
 - Lowest amount of CPU usage.
 - Lowest amount of RAM usage.
 - Lowest amount of temporary file space.
 - Lowest amount of external dependencies.
 - Lowest amount of lines of code.
 - Personal Preference.

To make sure that scoring is done fairly, for each of the above points each
PR is ordered and point are reversed given (this is done by each member of the
team individually).

For example if there are three PR's then for the first item (names), the best
PR gets 3 points, the second one 2 points and the third one 1 point.
If there is a tie for first place then both of them get 2 points and the third
gets 1 point. If there is a tie for second place then the first one get 3 points
and the other get 1 point each.

Then all points for each PR are counted up, the PR with the most points wins.
If there is still a tie for first place than the oldest PR (measured by last
commit) wins.
