# Autotodo
------

### Why maintain your own TODO files?
Keeping documentation up-to-date is tough, non-source files such as a TODO file will not break code if it is left stale, which is why generally these files are the last to be updated.

Keeping fresh TODO file allows users to informed on which tasks are yet to be done, 
without relying on third-party issue tracking software.

Even using third-party issue tracking software requires maintainance.

### Why not generate TODO tasks automagically with simple source code comments?
Autotodo is a source code parser that extracts TODO source code lines and outputs
a TODO file with surrounding source code pointing to source of undone tasks

Implemented in python 2 using standard library features

Currently targarted for C++ style comments

Licensed with BSD 3-Clause

Written by Jason Quisberth
