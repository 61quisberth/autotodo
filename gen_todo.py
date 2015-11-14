#/bin/python

# parse repo tree, collect todo's, generate todo file

# Unix tool inspiration
# grep, sed, cut, awk

import os
import os.path
import sys
import re

# single file grepping class
class Grepper:
  def __init__(self):
    self.matches = {}
    self.is_empty = True

  # pseudo grep method
  def grep_file(self, filename, pattern):
    fid = open(filename, "r")
    line_cnt = 0
    for line in fid:
      line_cnt = line_cnt+1
      if re.search(pattern, line):
        return filename + ":" + str(line_cnt) + ':' + line.strip('\n')

  # traverse root directory, and list directories as dirs and files as files
  def walk_print(self, dir_in):
    file_tup = [];
    for root, dirs, files in os.walk(dir_in):
      path = root.split('/')
      for file in files:
        file_tup.append((root + "/" + file))
    return file_tup

  # alt to grep_file, ex using regex
  def regex_tester():
    r = re.compile('^[0-9]*$')
    string_list = ['123', 'a', '467','a2_2','322','21']
    return filter(r.match, string_list)

  # writing todo file
  def populate_todo(self, base_dir):
    pat = "TODO:"
    fo = open("TODO", "wb")
    for file_mat in self.walk_print(base_dir): 
      if ( self.grep_file(file_mat, pat) ):
        fo.write( self.grep_file(file_mat, pat)  + '\n')
    fo.close()


# main 

if (len(sys.argv) != 2):
  print "usage: " + sys.argv[0] + " <search_dir_name>" 
  print 'Argument List:', str(sys.argv)
  sys.exit(2)

g0 = Grepper()

g0.populate_todo(sys.argv[1])

print "TODO file generated via Autotodo"
