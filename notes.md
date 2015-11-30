 Potential Read Program via http://bioinform.github.io/metasv/
 Video at http://www.bina.com


Viewing differences between local and cached:
 >>> git diff --cached --name-only


~~ Python Docstring for later ~~

############
##  INFO  ##
############
#  Summary:    With source genome reads of pacbio and illumina paired, we will seek to assemble
#              the fragmented reads using spades

# usage: main.py [-h] [-v] [matrixFileName] [FASTAFileName]
# * Raises errors as the specs required. Logs generated to log.txt *

# Displays an alignment score matrix and two aligned sequences from a score matrix and FASTA file.

# positional arguments:
#   m              the scoring matrix for alignments
#   FASTA          a FASTA file with at least 2 sequences

# optional arguments:
#   -h, --help     show this help message and exit
#   -v, --verbose  Displays traversedMatrix if True

#############
##  NOTES  ##
#############
# Ready to run!
#  > python main.py sample_matrix.txt sample_input.fa
# 1. Reads in matrix and FASTA files and handles errors
# 2. Writes composition log messages to log.txt
# 3. Pass in the -v flag to print the path tracemap to stdout

#############
##  STEPS  ##
#############
# a. Read FASTA
#    - return 2 sequences as a list (length 2) of strings
# b. Read matrix
#    - return a scoreMatrix instance with keys, values, and gapPenalty
# c. Create Alignment Score Matrix
#    - calls readFASTA and readMatrix
#    - Generates scoreMatrix with algorithm
#        ** Go row by row (or column by column) filling in each cell value with the maximum of **
#            1. The value from above - the gap penalty
#            2. The value from the cell diagonally up and left + the value from the similarity matrix of aligning the two characters for the current cell
#            3. The value from the left - the gap penalty
#    - returns traceMap as well for speed
# d. Reconstruct path
#    - load max value from the last col of the  AlignmentscoreMatrix
#    - traverse to create path
