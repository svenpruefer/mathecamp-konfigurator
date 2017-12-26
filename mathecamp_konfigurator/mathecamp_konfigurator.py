# -*- coding: utf-8 -*-

"""Main module."""

###########
# Imports #
###########

import argparse

##########
# Launch #
##########

parser = argparse.ArgumentParser()
parser.add_argument("--file", help = "This argument is the relative path to the file for reading and saving data. "
                                     "Only text "
                            "files with semicolon separated input are accepted. See the documentation for more "
                            "information.")
arguments = parser.parse_args()

####################
# Main entry point #
####################

def main(args):
    print(args)
    
main(arguments)

