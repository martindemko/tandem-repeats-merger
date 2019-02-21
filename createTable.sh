# Copyright (C) 2016 by Zdenka Sedenka <zdenka@sedenka.cz>
TEMPFILE=/tmp/$$.tmp
echo "" > $TEMPFILE
cd $1
mkdir res
for FILE_NAME in *.txt	
do 
(	
  echo 'run script'$FILE_NAME
  echo $(cat $TEMPFILE)
  IN_NAME=${FILE_NAME%.*}                   
  sed 's/\r$//' $PWD"/"$IN_NAME".txt" > "res/"$IN_NAME".txt"
  sort -k 2 "res/"$IN_NAME".txt" > "res/"$IN_NAME"_sorted.txt"
  echo $IN_NAME" A" > "res/"$IN_NAME"_sorted_first.txt"
  cat "res/"$IN_NAME"_sorted.txt" >> "res/"$IN_NAME"_sorted_first.txt"   
)
done
unlink $TEMPFILE

