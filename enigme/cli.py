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
from .gridbased import generate_fraction_puzzle
from .gridbased import grid_print_string
from .gridbased import generate_rotation_puzzle
from .seqbased import generate_sequence_puzzle
from .seqbased import generate_2d_physics_puzzle
from .gridbased import get_structure_print_string
 
##########################################################################################
def print_usage(prog):
    """ Command line application usage instrutions. """
    print(" USAGE ")
    print(" ", prog, "[OPTIONS] <COMMAND>")
    print("   <COMMAND>                 - PUZZLE CLASS [ frac | 1d | 2d | 3d ]")
    print("   [OPTIONS]")
    print("      -v, --version          - Print version")
    print("      -h, --help             - Get command help")
    print("")


##########################################################################################
def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('-v', '--version', help='Print Version', action='store_true')
   parser.add_argument('-u', '--usage', help='More detailed usage information', action='store_true')
   parser.add_argument('puzzle', help='Puzzle class: [ frac | 1d | 2d | 3d ]')

   args = parser.parse_args()

   if args.version:
       print(" Version:", __version__)
       exit(1)

   if args.usage:
       print_usage("enigme")
       exit(1)

   if args.puzzle=='frac':
      print_frac_puzzle()
   if args.puzzle=='1d':
       print_seq_puzzle()
   if args.puzzle=='2d':
       print_grid_puzzle()



##########################################################################################
def print_grid_puzzle():
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
def print_frac_puzzle():
   fore, str1, numer, denom = generate_fraction_puzzle()
   print()
   print(f"What fraction of the chracaters in this grid are {fore}?")
   print()
   print(grid_print_string(str1))
   print()
   print("Press a key when you are ready to continue and see the answer...")
   input()
   answer_str = f"Answer:  {numer}/{denom}"
   print(answer_str)
   #print("   O O O X O O")
   #print("   O O O X O O")
   #print("   O O O X O O")
   #print("   X O O X O X")


##########################################################################################
def print_seq_puzzle():
   str1, str2, str3, str4 = generate_sequence_puzzle()
   print()
   print("Below you will see 3 strings of characters that form a pattern. What is the next pattern in the sequence?")
   print()
   print("    |" + ("".join(str1)) + "|")
   print("    |" + ("".join(str2)) + "|")
   print("    |" + ("".join(str3)) + "|")
   print("    ")
   print("Press a key when you are ready to continue and see the answer...")
   print()
   input()
   print("    |" + ("".join(str4)) + "|" )



##########################################################################################
if __name__ == '__main__':
    main()
