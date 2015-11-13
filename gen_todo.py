#/bin/python

# parse repo tree, collect todo's, generate todo file

# Unix tool inspiration
# grep, sed, cut, awk

import os
import os.path
import re
import sys

# single file grepping class
class grepper:
  def __init__(self):
    self.matches = {}
    self.is_empty = True


  # dummy method writing todo file
  def write_to_todo():
    fo = open("TODO", "wb")
    fo.write( "TODO: implement logic to auto-populate this file\n");
    fo.close()

  # pseudo grep method
  def grep_file(filename, pattern):
    file = open(filename, "r")
    line_cnt = 0
    for line in file:
      line_cnt = line_cnt+1
      if re.search(pattern, line):
        return str(line_cnt) + ':' + line.strip('\n')

  # psuedo tree method
  def print_walk(dir_in):
    # os.walk uses a tuple of root-dirs-files
    for root, dirs, files in os.walk(dir_in):
      return files #dictionary of files

  def regex_tester():
    r = re.compile('^[0-9]*$')
    string_list = ['123', 'a', '467','a2_2','322','21']
    return filter(r.match, string_list)


# main 
g0 = grepper()
print g0.is_empty
