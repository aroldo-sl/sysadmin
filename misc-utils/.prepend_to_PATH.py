#!/usr/bin/env python3
import os
import sys
# Prepends this script's arguments to the
# content of the $PATH environment variable and prints the
# resulting string to the standard output console.
# It doesn' really change of the contento of the actual
# system $PATH variable. A Bash script has to catch this
# script's output in order to do the actual resetting of
# $PATh.
dirs=sys.argv[1:]
PATH=os.environ.get("PATH")
if not dirs:
    print("No directories added to PATH")
    print("PATH={PATH}".format(PATH=PATH))
    sys.exit(0)
# from PATH as a string to PATH as a list:
PATH=PATH.split(os.pathsep)
for dir in dirs:
    if not dir in PATH:
        # prepending
        PATH.insert(0,dir)
# from PATH as a list to PATH as a sring:
PATH=os.pathsep.join(PATH)
print(PATH)