# Copyright (C) 2016 by Zdenka Sedenka <zdenka@sedenka.cz>
shortName="some_identiver"  # short identifier for your results, e.g. "15_cutAd_wd"
minNumberOfRepeats="3" # min number of repeats
minLengthOfPattern="4" # min length of pattern
dataDir="/my/data" # data dir

myDir="res"
mkdir $myDir

echo "trf"
sh iterateTRF.sh $myDir"/"$dataDir $myDir"/res_taref_"$shortName

echo "iterateAllFiles"
python iterateAllFiles.py -i $myDir"/res_taref_"$shortName -r $myDir"/parsedNonPerfect_"$shortName"_min"$minNumberOfRepeats"repeats_min"$minLengthOfPattern"pattern" -n $minNumberOfRepeats -p $minLengthOfPattern

echo "createTable"
sh createTable.sh $myDir"/parsedNonPerfect_"$shortName"_min"$minNumberOfRepeats"repeats_min"$minLengthOfPattern"pattern"

echo "join"
bash join.sh $myDir"/parsedNonPerfect_"$shortName"_min"$minNumberOfRepeats"repeats_min"$minLengthOfPattern"pattern/res"

echo "group cyclic permutations"
python removePermutations.py -f $myDir"/parsedNonPerfect_"$shortName"_min"$minNumberOfRepeats"repeats_min"$minLengthOfPattern"pattern/res/joined.txt"

echo "group reverse complements"
python modifyTableReverseComplement.py -f $myDir"/parsedNonPerfect_"$shortName"_min"$minNumberOfRepeats"repeats_min"$minLengthOfPattern"pattern/res/joined_fixed.txt"
 
echo "restrZeros"
python restrZeros.py -f $myDir"/parsedNonPerfect_"$shortName"_min"$minNumberOfRepeats"repeats_min"$minLengthOfPattern"pattern/res/joined_fixed_pairedReverseComplement.txt" -s 0 -b 1 -z 1 -r 0
python restrZeros.py -f $myDir"/parsedNonPerfect_"$shortName"_min"$minNumberOfRepeats"repeats_min"$minLengthOfPattern"pattern/res/joined_fixed_pairedReverseComplement.txt" -s 0 -b 2 -z 2 -r 0
python restrZeros.py -f $myDir"/parsedNonPerfect_"$shortName"_min"$minNumberOfRepeats"repeats_min"$minLengthOfPattern"pattern/res/joined_fixed_pairedReverseComplement.txt" -s 0 -b 3 -z 3 -r 0

