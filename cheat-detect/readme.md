Simple Cheat Detector
====================================================================================================

A simple cheat detector script which can provide some insight into cases for direct copying of
assignments.

This program will compare all given singular input files in the specified directory with one another
and compare them.

Based on a given `closeness factor`, the program will output an HTML diff of files which appear to
be similar.

Finally, output is provided which can be loaded into Excel to see the similarities between all
inputs.  The lowest, average, and highest comparison values will be provided as well.

To run, use Python 2:

    python cd.py config.txt

**Note**: This can take a long time to process.  It's best to leave it running unattended for a
while.


Options
--------

### Start Path

    STARTPATH = r'example'

The starting directory to look for input files.  Will recursively search subdirectories.  You can
specify a `..\` at the start to navigate up parents folders first.

### Skip Paths

    SKIPPATHS = [] # actually subtrees

Paths to skip when searching.

### Extensions

    EXTS = ['java']

List of extensions to take as input.

### Output file name

    RESULTFILE = r'result.tsv'

This file is a tab separated file which can be loaded in Excel.  The diagonal will be marked NA as
entries aren't compared to themselves.  You can highlight the inner matrix and select `Conditional
Formatting` -> `Color Scales` -> `Red - White` to get a clear picture of likely copies.

### Closeness Factor

    CLOSENESSFACTOR = 0.93

This value represents the threshold for two files to be similar in order to output a diff of the two
files.  These diffs will be output to the same location the script is running.  They can be loaded
in the browser to see the differences in the similar files.

### Auto Junk

    AUTOJUNK = False

Parameter for special 'junk' heuristic. See [Python Docs].



[Python Docs]: https://docs.python.org/2/library/difflib.html
