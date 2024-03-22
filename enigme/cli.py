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

##########################################################################################
if __name__ == '__main__':
    main()
