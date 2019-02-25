# Tandem Repeats Merger

Scripts for modifying output of Tandem Repeats Finder (TRF). 

Finds candidate telomeric sequences in NGS data output of TRF. 

Tested on Ubuntu 16.04 with Python 2.7. 

Either you can run TRM along with TRF starting with the .fasta files, or if you already have NGS output data from TRF, you can run the TRM only.

## How to run together with TRF

1. Place your data in .fasta format into one folder (e.g. ./data/)

2. Download Tandem Repeats Finder from https://tandem.bu.edu/trf/ and place it into this folder. If your binary is not named `trf407b.linux64` or you want to use different path than `$PWD`, modify `iterateTRF.sh`. 

Better solution is to use conda with the env.yaml configuration file. Just call `conda create env -f ./env.yaml -n trm-env` and after the installation process call `source activate trm-env`.

3. Change the variable `dataDir` inside the `./scripts/runAllWithTRF.sh` to point into your directory with inpout data. You may also want to change the default name of output data (variable `shortName`). In the very same script, one can see the default settigns of other input parameters. They can be changed inside the script or sent from command line as follows: `./runAllWithTRF.sh 3 4 2 7 7 80 10 50 15 2 90 0 -h`. It will create specific folder structure.

## How to run without TRF

1. Assuming you already have TRF's NGS output data, you should place them into `./scripts/res/TRF\_res` directory with `.dat` extension.

2. You may also change the variable `myDir` inside the `./scripts/runAllNoTRF.sh` script so you can place your input data accordingly into `${myDir}/TRF\_res` directory.

3. This particular script has much less input paramaters to set. They can be changed inside the script or sent from command line as follows: `./runAllNoTRF.sh 3 4 90 0`. It will create specific folder structure.

## Explain the input parameters

All the input parameters are contained together in the `runAllWithTRF.sh` script so we use here the explanation from there (so far, they must be used in the specified order and in the right place):

* __minNumberOfRepeats="3"__   ... min number of repeats
* __minLengthOfPattern="4"__   ... min length of repeating pattern
* __trf_match="2"__            ... TRF's matching weight
* __trf_mism="7"__             ... TRF's mismatching penalty
* __trf_delta="7"__            ... TRF's indel penalty
* __trf_pm="80"__              ... TRF's match probability (whole number)
* __trf_pi="10"__              ... TRF's indel probability (whole number)
* __trf_min="50"__             ... TRF's minimum alignment score to report
* __trf_max="15"__             ... TRF's maximum period size to report
* __trf_longest="2"__          ... TRF's maximum TR length expected (in millions)
* __readLength="90"__          ... for restrZeros.py
* __relOccur="0"__             ... if yes, the value must be 1 otherwise it is preset to 0
* __trf_html=""__              ... TRF's html output; if you want to supress it change the value to '-h'

## Explain specific output folder structure


* __res__                                                                              ... predifined output directory name (can be changed in the variable `myDir` in the scripts `runAllWithRTF.sh` and `runAllNoTRF.sh`)
  * __parsed__
    * __dataset\_6484\_ppr.txt__                                                   ... intermediate file
    * __dataset\_6485\_ppr.txt__                                                   ... intermediate file
    * __dataset\_6486\_ppr.txt__                                                   ... intermediate file
    * __res__
      * __dataset\_6484\_ppr\_sorted.txt__                                       ... intermediate file
      * __dataset\_6485\_ppr\_sorted.txt__                                       ... intermediate file
      * __dataset\_6486\_ppr\_sorted.txt__                                       ... intermediate file
      * __joined\_fixed\_pairedReverseComplement\_merged\_sorted\_FINAL.txt__    ... FINAL output file with reverse-complement-paired sequences of tandem repeats with number of occurrences in the input datasets 
      * __joined\_fixed\_pairedReverseComplement\_merged\_sorted.txt__           ... intermediate file
      * __joined\_fixed\_pairedReverseComplement\_merged.txt__                   ... intermediate file
      * __joined\_fixed\_pairedReverseComplement.txt__                           ... intermediate file
      * __joined\_fixed.txt__                                                    ... intermediate file
      * __joined\_fixed\_without\_pairedReverseComplement\_sorted_FINAL.txt__    ... FINAL output file sorted according to the number of occurrences of tandem repeats in the input datasets
      * __joined\_fixed\_without\_pairedReverseComplement\_sorted.txt__          ... intermediate file
      * __joined\_fixed\_without\_pairedReverseComplement.txt__                  ... intermediate file
      * __joined.txt__                                                           ... intermediate file
  * __TRF\_res__                                                                     ... directory containing all TRF outputs (either it is filled automatically (case of `runAllWithTRF.sh`), or you must copy your input here (case of `runAllNoTRF.sh`)
    * __dataset\_6484.dat__                                                        ... NGS data from TRF
    * __dataset\_6485.dat__                                                        ... NGS data from TRF
    * __dataset\_6486.dat__                                                        ... NGS data from TRF



