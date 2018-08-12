"""
Auto Cheat Detector
"""
__version__ = '1.0'
__author__ = 'Michael A. Hawker'

# PROGRAM DEFAULTS
STARTPATH = r'example'
SKIPPATHS = []
EXTS = ['java']
RESULTFILE = r'result.txt'
CLOSENESSFACTOR = 0.95
AUTOJUNK = False

import fnmatch
import sys
import time
import os
import difflib
import string
import datetime
from shutil import copyfile
from subprocess import call

def main():
    """
    build file list, validate and print result
    """
    print 'Using config:'
    print '\tLocal files in:\n\t\t%s' % STARTPATH
    print '\tSkip directories:\n\t\t%s' % SKIPPATHS
    print '\tResult File:\n\t\t%s' % RESULTFILE
    print '\tCloseness:\n\t\t%s (IGNORE JUNK %s)' % (CLOSENESSFACTOR, AUTOJUNK)
    #print '\tError Reports are saved to\n\t\t%s' % REPORTDIR
    print '-' * 40
    start = time.time()

    # find files to validate
    files = []
    for dir, dirs, fs in os.walk(STARTPATH):
        skip = False
        for sp in SKIPPATHS:
            if dir.startswith(os.path.join(STARTPATH, sp)):
                skip = True
                break
        if not skip:
            for ext in EXTS:
                names = fnmatch.filter(fs, '*.%s' % ext)
                names.sort()
                dirfile = [(dir, n) for n in names if n.find('.ERR') == -1]
                files.extend(dirfile)

    results = open(RESULTFILE, "w")
    results.write("RESULTS " + str(datetime.datetime.now()) + "\n")

    # top of grid
    results.write("\t")
    for fpath, fname in files:
        results.write(os.path.join(fpath, fname) + "\t")
    results.write("\n")

    low = 1.0
    high = 0.0
    num = 0
    total = 0.0
    
    # validate
    for fpath, fname in files:
        abspath = os.path.join(fpath, fname)
        results.write(abspath+"\t")
        print "Comparing " + abspath
        for fpath2, fname2 in files:            
            abspath2 = os.path.join(fpath2, fname2)

            if abspath == abspath2:
                results.write("NA\t")
                continue
            
            num += 1
            print "\tTo " + abspath2,

            # open files
            file1 = open(abspath, "r")
            file2 = open(abspath2, "r")

            contents1 = file1.readlines()
            contents2 = file2.readlines()

            file1.close()
            file2.close()

            r = difflib.SequenceMatcher(lambda x: x in string.whitespace, string.join(contents1, "\n"), string.join(contents2, "\n"), AUTOJUNK).ratio()
            print repr(r)
            results.write(repr(r) + "\t")

            if r < low:
                low = r
            if r > high:
                high = r

            total += r
            avg = total / num

            if r > CLOSENESSFACTOR or (r > avg and num > 1):
                diffout = open(os.path.splitext(fname)[0] + "." + os.path.splitext(fname2)[0] + ".diff.htm", "w")
                diffout.write(difflib.HtmlDiff().make_file(contents1, contents2))
                diffout.close()
            #for
        #for
        results.write("\n")
    #print summary    

    print
    print '-' * 40
    print 'Finished %d files in %.2f sec.' % (len(files), time.time() - start)
    print '%d Comparisons: %.2f low, %.2f avg, %.2f high' % (num, low, avg, high)

    results.write('%d Comparisons: %.2f low, %.2f avg, %.2f high' % (num, low, avg, high) + "\n")
    results.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Usage: python cd.py config.txt\n'
    else:
        config = open(sys.argv[1]).read()
        exec(config)
    main()
