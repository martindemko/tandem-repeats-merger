shortName="data"  # short identifier for your results, e.g. "15_cutAd_wd"
dataDir="data" # data dir
## setable parameters:
## defaults
minNumberOfRepeats="3" # min number of repeats
minLengthOfPattern="4" # min length of pattern
readLength="90" # for restrZeros.py
relOccur="0"	# if yes, the value must be 1 otherwise it is preset to 0

minNumberOfRepeats="$1" # min number of repeats
minLengthOfPattern="$2" # min length of pattern
readLength="${3}" # for restrZeros.py
relOccur="${4}"	# if yes, the value must be 1 otherwise it is preset to 0

myDir="res"

echo "iterateAllFiles"
python iterateAllFiles.py -i $myDir"/TRF_res/" -r $myDir"/parsed" -n $minNumberOfRepeats -p $minLengthOfPattern

echo "createTable"
bash createTable.sh $myDir"/parsed"

echo "join"
bash join.sh $myDir"/parsed/res" "$dataDir"

echo "group cyclic permutations"
python removePermutations.py -f $myDir"/parsed/res/joined.txt"

echo "group reverse complements"
python modifyTableReverseComplement.py -f $myDir"/parsed/res/joined_fixed.txt"

echo "sort"
cd $myDir"/parsed/res"
#sed -i '1a \\' joined_fixed_pairedReverseComplement.txt
#awk ' /^$/ { print; } /./ { printf("%s ", $0); }' joined_fixed_pairedReverseComplement.txt > joined_fixed_pairedReverseComplement_merged.txt
awk '{print $NF,$0}' joined_fixed_pairedReverseComplement_merged.txt  | sort -nr | cut -f2- -d' ' > joined_fixed_pairedReverseComplement_merged_sorted.txt
#sed '1h;1d;$!H;$!d;G' joined_fixed_pairedReverseComplement_merged_sorted.txt > joined_fixed_pairedReverseComplement_merged_sorted_FINAL.txt
grep "^Sequence" joined_fixed_pairedReverseComplement_merged_sorted.txt > joined_fixed_pairedReverseComplement_merged_sorted_FINAL.txt
grep -v "^Sequence" joined_fixed_pairedReverseComplement_merged_sorted.txt >> joined_fixed_pairedReverseComplement_merged_sorted_FINAL.txt || echo "empty file with paired"

awk '{print $NF,$0}' joined_fixed_without_pairedReverseComplement.txt  | sort -nr | cut -f2- -d' ' > joined_fixed_without_pairedReverseComplement_sorted.txt
#sed '1h;1d;$!H;$!d;G' joined_fixed_without_pairedReverseComplement_sorted.txt > joined_fixed_without_pairedReverseComplement_sorted_FINAL.txt
grep "^Sequence" joined_fixed_without_pairedReverseComplement_sorted.txt > joined_fixed_without_pairedReverseComplement_sorted_FINAL.txt
grep -v "^Sequence" joined_fixed_without_pairedReverseComplement_sorted.txt >> joined_fixed_without_pairedReverseComplement_sorted_FINAL.txt || echo "empty file without paired"


### not needed in most cases
# echo "restrZeros"
# subst=""
# for name in "$dataDir"/*; do subst=${subst}"`grep ">" $name | wc -l`,"; done
# # use as ${subst%,} to get rid of the final comma
# sed -i -e "/numberOfReads[[:space:]]*=/ s/\[[^]]*\]/[${subst%,}]/" restrZeros.py
# sed -i -e "s/readLength[[:space:]]*=[[:space:]]*[[:digit:]]*/readLength = ${readLength}/" restrZeros.py
# python restrZeros.py -f $myDir"/parsed/res/joined_fixed_pairedReverseComplement.txt" -s 0 -b 1 -z 1 -r "$relOccur"
# python restrZeros.py -f $myDir"/parsed/res/joined_fixed_pairedReverseComplement.txt" -s 0 -b 2 -z 2 -r "$relOccur"
# python restrZeros.py -f $myDir"/parsed/res/joined_fixed_pairedReverseComplement.txt" -s 0 -b 3 -z 3 -r "$relOccur"

