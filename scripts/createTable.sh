#!/bin/bash
cd $1
mkdir "res"
for FILE_NAME in *.txt; do
  echo "sorting $FILE_NAME"
  IN_NAME=${FILE_NAME%.*}
  echo "${IN_NAME%_ppr} Sequence" > "${PWD}/res/"$IN_NAME"_sorted.txt"
  sed 's/\r$//' "${PWD}/${IN_NAME}.txt" | sort -k 2  >> "${PWD}/res/${IN_NAME}_sorted.txt"
done

