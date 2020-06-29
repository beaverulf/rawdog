#!/usr/bin/python
import os
import sys
import argparse

rw2 = ".RW2"
jpg = ".JPG"
dotmov = ".MOV"
dotmp4 = ".MP4"

videoTypes = [ dotmp4, dotmov ]
photoTypes = [ rw2, jpg ]

parser = argparse.ArgumentParser(description='Handle imported camera files')
parser.add_argument('-d', dest="directory", default=".", type=str, nargs='?', help='directory to parse')
parser.add_argument("-rm", action="store_true", dest="delete", help="delete raws")
parser.add_argument("-s","--sort", action="store_true", dest="sort", help="seperate videos and photos")
args = parser.parse_args()


def rawDog():
    files = os.listdir(args.directory)
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
    photos = "photos"
    videos = "videos"
    os.mkdir(videos)
    os.mkdir(photos)

    files = os.listdir(args.directory)
    
    for file in files:
        filetype = os.path.splitext(file.upper())[1]
        if filetype in videoTypes:
            os.rename(file, videos + "/" + file)
        if filetype in photoTypes:
            os.rename(file, photos + "/" + file)
        
if __name__ == "__main__":
    if args.delete:
        rawDog()
    elif args.sort:
        sortFiles()
    else: parser.print_help()
    