#!/usr/bin/python
# Bioinformatics Pipeline

import sys
import os
import subprocess

print("BIOINFORMATICS PIPELINE")
pathMaster = raw_input("Enter the path to the master file (which contains the file paths in the order you want to execute them on separate lines): ")

if not os.path.isfile( pathMaster ):
    sys.stderr.write('Exiting pipeline execution. Specified path to master file is NOT a file.\n')
    raise SystemExit(1)

fileList = [line.rstrip() for line in open( pathMaster )]
for filepath in fileList:
   if not os.path.isfile( filepath ):
    sys.stderr.write("Exiting pipeline execution. Specified path in master file is NOT a file: " + filepath)
    raise SystemExit(1)


print("Filepaths: " + str(fileList))
fiPathsCorrect = raw_input("Are these file paths correct? [Y/N] ")
if fiPathsCorrect not in ('Y','y'):
    sys.stderr.write('Exiting pipeline execution. File paths not confirmed.\n')
    raise SystemExit(1)

print('')

try:
    for filepath in fileList:
        subprocess.call(['python', filepath])

    print ("\nBioinformatics pipeline completed successfully.")
except Exception as e:
    sys.stderr.write("Error: " + e)
    raise SystemExit(1)