#!/usr/bin/env python3
"""Separates Altera's junky concatenated CSV files into unique files

We do this in two steps:
1. Move all existing *.txt files to *.tmp files
2. Go through and break up at the start of each CSV file into a new file
"""

import os
import sys

from pathlib import Path


def main(root: str):
    root_path = Path(root)
    orig_files = [f for f in root_path.glob('*.txt')]
    for orig_file in orig_files:
        os.rename(orig_file, orig_file.with_suffix('tmp'))

    orig_files = [f for f in root_path.glob('*.tmp')]
    for orig_file in orig_files:
        idx = 0
        new_file_name = orig_file.parent.joinpath(orig_file.stem + '-' +
                                                  str(idx) + '.txt')
        new_file = open(new_file_name, 'w')

        with open(orig_file, 'r', encoding='cp1252') as orig:
            lines = orig.readlines()

            for line in lines:
                if line.startswith('Bank'):
                    new_file.close()
                    idx = idx + 1
                    new_file_name = orig_file.parent.joinpath(
                        orig_file.stem + '-' + str(idx) + '.txt')
                    new_file = open(new_file_name, 'w')
                    new_file.write(line)
                else:
                    new_file.write(line)

        new_file.close()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(os.getcwd())
    elif len(sys.argv) == 2:

        main(sys.argv[1])
    else:
        print("Wrong number of args.")
