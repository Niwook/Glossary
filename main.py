#!/usr/bin/python3

"""Start application"""
import os
import sys
import index


if __name__ == "__main__":
    os.system('clear')
    # Resizing terminal width and height
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=100))
    index.main()
