#/bin/python

# parse repo tree, collect todo's, generate todo file

# Unix tool inspiration
# grep, sed, cut, awk

import os
import os.path
import re
import sys

# single file grepping class
class Grepper:
  def __init__(self):
    self.matches = {}
    self.is_empty = True


  # dummy method writing todo file
  def write_to_todo():
    fo = open("TODO", "wb")
    fo.write( "TODO: implement logic to auto-populate this file\n");
    fo.close()

  # pseudo grep method
  def grep_file(self, filename, pattern):
    file = open(filename, "r")
    line_cnt = 0
    for line in file:
      line_cnt = line_cnt+1
      if re.search(pattern, line):
        return filename + ":" + str(line_cnt) + ':' + line.strip('\n')

  # traverse root directory, and list directories as dirs and files as files
  def walk_print(self, dir_in):
    file_tup = [];
    for root, dirs, files in os.walk("./test"):
      path = root.split('/')
      for file in files:
        file_tup.append((root + "/" + file))
    return file_tup

  def regex_tester():
    r = re.compile('^[0-9]*$')
    string_list = ['123', 'a', '467','a2_2','322','21']
    return filter(r.match, string_list)


# main 
g0 = Grepper()

# test grep impl
#filename = "/Users/jason_quisberth/work/autotodo/test/src/hello.cc"
filename = "./test/src/hello.cc"
pat = "TODO:"
print g0.grep_file(filename, pat)

print ""

# test tree impl
print g0.walk_print(".")
