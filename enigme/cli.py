import argparse
import pandas as pd
import numpy as np
import sys
import os

# -*- coding: utf-8 -*-
  
"""
   enigme.cli: Command line interface for enigme puzzle generation.
"""

from enigme import __version__
from .gridbased import generate_rotation_puzzle
from .gridbased import get_structure_print_string
 
##########################################################################################
def print_usage(prog):
    """ Command line application usage instrutions. """
    print(" USAGE ")
    print(" ", prog, "[OPTIONS] <COMMAND>")
    print("   <COMMAND>     - CORE TASK TO PERFORM: [init | upate | rm | status | add | list | compare | render]")
    print("   [OPTIONS]")
    print("      -v, --version          - Print version")
    print("      -h, --help             - Get command help")
    print("")


##########################################################################################
def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('-v', '--version', help='Print Version', action='store_true')
   parser.add_argument('-u', '--usage', help='More detailed usage information', action='store_true')

   args = parser.parse_args()

   if args.version:
       print(" Version:", __version__)
       exit(1)

   if args.usage:
       print_usage("enigme")
       exit(1)

   str1, str2, str3, str4 = generate_rotation_puzzle()

   print()
   print("Below you will see 3 patterns that form a sequence. Write down the expected 4th pattern in the sequence.")
   puzzle_str = get_structure_print_string([str1, str2, str3])
   print(puzzle_str) 
   print()
   print("Press a key when you are ready to continue and see the answer...")
   print()
   input()
   answer_str = get_structure_print_string([str4], 4)
   print(answer_str)

 
##########################################################################################
if __name__ == '__main__':
    main()
