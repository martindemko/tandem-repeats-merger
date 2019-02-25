# Tandem Repeats Merger

Scripts for modifying output of Tandem Repeats Finder (TRF). 

Finds candidate telomeric sequences in NGS data output of TRF. 

Tested on Ubuntu 16.04 with Python 2.7. 

Either you can run TRM along with TRF starting with the .fasta files, or if you already have NGS output data from TRF, you can run the TRM only.

## How to run together with TRF

1. Place your data in .fasta format into one folder (e.g. ./data/)

2. Download Tandem Repeats Finder from https://tandem.bu.edu/trf/ and place it into this folder. If your binary is not named trf407b.linux64 or you want to use different path than $PWD, modify iterateTRF.sh. 

Better solution is to use conda with the env.yaml configuration file. Just call `conda create env -f ./env.yaml -n trm-env` and after the installation process call `source activate trm-env`.

3. Change the variable `dataDir` inside the `./scripts/runAllWithTRF.sh` to point into your directory with inpout data. You may also want to change the default name of output data (variable `shortName`). In the very same script, one can see the default settigns of other input parameters. They can be changed inside the script or sent from command line as follows: `./runAllWithTRF.sh 3 4 2 7 7 80 10 50 15 2 90 0 -h`. It will create specific folder structure.

## How to run without TRF

1. Assuming you already have TRF's NGS output data, you should place them into `./scripts/res/TRF\_res` directory with `.dat` extension.

2. You may also change the variable `myDir` inside the `./scripts/runAllNoTRF.sh` script so you can place your input data accordingly into `${myDir}/TRF\_res` directory.

3. This particular script has much less input paramaters to set. They can be changed inside the script or sent from command line as follows: `./runAllNoTRF.sh 3 4 90 0`. It will create specific folder structure.

## Explain the input parameters

All the input parameters are contained together in the `runAllWithTRF.sh` script so we use here the explanation from there (so far, they must be used in the specified order and in the right place):

* minNumberOfRepeats="3"   # min number of repeats
* minLengthOfPattern="4"   # min length of repeating pattern
* trf_match="2"            # TRF's matching weight
* trf_mism="7"             # TRF's mismatching penalty
* trf_delta="7"            # TRF's indel penalty
* trf_pm="80"              # TRF's match probability (whole number)
* trf_pi="10"              # TRF's indel probability (whole number)
* trf_min="50"             # TRF's minimum alignment score to report
* trf_max="15"             # TRF's maximum period size to report
* trf_longest="2"          # TRF's maximum TR length expected (in millions)
* readLength="90"          # for restrZeros.py
* relOccur="0"             # if yes, the value must be 1 otherwise it is preset to 0
* trf_html=""              # TRF's html output; if you want to supress it change the value to '-h'

## Explain specific output folder structure


* res                                                                              ... predifined output directory name (can be changed in the variable `myDir` in the scripts `runAllWithRTF.sh` and `runAllNoTRF.sh`)
* ├── parsed
* │   ├── dataset\_6484\_ppr.txt                                                   ... intermediate file
* │   ├── dataset\_6485\_ppr.txt                                                   ... intermediate file
* │   ├── dataset\_6486\_ppr.txt                                                   ... intermediate file
* │   └── res
* │       ├── dataset\_6484\_ppr\_sorted.txt                                       ... intermediate file
* │       ├── dataset\_6485\_ppr\_sorted.txt                                       ... intermediate file
* │       ├── dataset\_6486\_ppr\_sorted.txt                                       ... intermediate file
* │       ├── joined\_fixed\_pairedReverseComplement\_merged\_sorted\_FINAL.txt    ... FINAL output file
* │       ├── joined\_fixed\_pairedReverseComplement\_merged\_sorted.txt           ... intermediate file
* │       ├── joined\_fixed\_pairedReverseComplement\_merged.txt                   ... intermediate file
* │       ├── joined\_fixed\_pairedReverseComplement.txt                           ... intermediate file
* │       ├── joined\_fixed.txt                                                    ... intermediate file
* │       ├── joined\_fixed\_without\_pairedReverseComplement\_sorted_FINAL.txt    ... FINAL output file
* │       ├── joined\_fixed\_without\_pairedReverseComplement\_sorted.txt          ... intermediate file
* │       ├── joined\_fixed\_without\_pairedReverseComplement.txt                  ... intermediate file
* │       └── joined.txt                                                           ... intermediate file
* └── TRF\_res                                                                     ... directory containing all TRF outputs (either it is filled automatically (case of `runAllWithTRF.sh`), or you must copy your input here (case of `runAllNoTRF.sh`)
*     ├── dataset\_6484.dat                                                        ... NGS data from TRF
*     ├── dataset\_6485.dat                                                        ... NGS data from TRF
*     └── dataset\_6486.dat                                                        ... NGS data from TRF



