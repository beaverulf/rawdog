#!/usr/bin/python
import os
import sys
import argparse

rw2 = ".RW2"
jpg = ".JPG"

parser = argparse.ArgumentParser(description='Handle imported camera files')
parser.add_argument('dir', type=str, nargs='?',
                    help='directory to parse')
parser.add_argument("-d", action="store_true", dest="delete", help="delete raws")
parser.add_argument("-s","--sort", action="store_true", dest="sort", help="seperate videos and photos")
args = parser.parse_args()

def rawDog(dir = "."):
    files = os.listdir(dir)
    orphaned = []

    #Find all raw files
    for file in files:
        if file.endswith(rw2):
            filename = os.path.splitext(file)[0]
            #If orphaned
            if filename + jpg not in files:
                orphaned.append(filename+rw2)

    #Delete orphaned raws
    if args.delete:
            print("Deleting "+str(len(orphaned))+" orphaned raw file(s).")
            for raw in orphaned:
                os.remove(raw)
    else:
        print("Found "+str(len(orphaned))+" orphaned raw file(s).")

def sortFiles():
    None
    
if __name__ == "__main__":
    rawDog()
    if args.sort:
        sortFiles()
    