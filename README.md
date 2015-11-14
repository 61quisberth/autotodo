# Autotodo
------

### Why maintain your own TODO files?
Keeping documentation up-to-date is tough, non-source files such as a TODO file will not break code if it is left stale, which is why generally these files are the last to be updated.

Keeping a fresh TODO file allows users to informed on which tasks are yet to be done, 
without relying on third-party issue tracking software.

Even using third-party issue tracking software requires maintainance.

### Why not generate TODO tasks automagically with simple source code comments?
Autotodo is a source code parser that extracts TODO source code lines and outputs
a TODO file for you!

A developer can now go through his/her development, mark TODO's as typical inline comments,
and run the program

Autotodo will recursively go though the passed argument and search for TODO inlne comments

### Installation
No installation required, just clone the repo for the script

### Usage
`python gen_todo.py <base_dir>`
`cat TODO`
`path_to_file_hit:line_numer: [source code line containing inline comment]`


Implemented in python 2 using standard library features
Licensed with BSD 3-Clause


Written by Jason Quisberth
