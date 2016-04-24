# Tandem Repeats Merger

Scripts for modifying output of Tandem Repeats Finder. 

Finds candidate telomeric sequences in NGS data, assuming you have BAL31-treated and untreated samples. 

Tested on Ubuntu 12.04 with Python 2.7. 

HOW TO RUN:

1. Place your data in .fasta format into one folder (e.g. /my/data)

2. Download Tandem Repeats Finder from https://tandem.bu.edu/trf/ and place it into this folder. If your binary is not named trf407b.linux64 or you want to use different path than $PWD, modify iterateTRF.sh. TRF parameters (”2 7 7 80 10 50 15”) can also be changed here. 
If you only want to do the post-processing, comment out iterateTRF.sh script in runAllTRF.sh

3. In runAllTRF.sh, set:
  data_dir=“/my/data"  # name of folder with your data
  short_name=“some_identifier”  # identifier for output folder names
  minNumberOfRepeats="3" # minimum number of repeats to consider
  minLengthOfPattern=“2”  # minimum length of pattern to consider

4. In join.sh, set "names” to exact names of your fasta files (without “.fasta” extension).
If you want to measure BAL31 sensitivity, you need to set “names” in order A_genom, A_bal, B_genom, B_bal, …

5. If you want to count relative occurrences, got to runAllTRF.sh and set -r 1 for python restrZeros.pyrestrZeros.py.
In restrZeros.py, set numberOfReads to correspond to your dataset (same order as in previous step in “names”). 
Set also the readLength. This assumes your reads were cut to same length.

6. Run! (This will take a while.)
   cd tandem-repeats-merger
   sh runAllTRF.sh

7. Check out your candidate telomeric sequences in tandem-repeats-merger/parsedNonPerfect_SHORTNAME_Nrepeats/res/joined_fixed_pairedReverseComplement_allowedZeros_ZZZ_allowedBal_BBB.txt
These are the sequences, which (1) have zero occurrences in data without BAL-31 in ZZZ or less species, and (2) have more occurrences in data with BAL-31 than without BAL-31 in BBB or less species. 

