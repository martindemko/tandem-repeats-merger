#!/bin/bash
# Copyright (C) 2016 by Zdenka Sedenka <zdenka@sedenka.cz>
# Joins files in folder $1 together, in order defined in names. The files were previously sorted by createTable.sh
cd $1
names=( A_Anglosum A_Anglosum_B A_Cepa A_Cepa_B )
echo ${names[0]}
if [ ${#names[@]} -gt 1 ] ;
then
	echo ${names[1]}
	if [ ${#names[@]} -gt 2 ]
	then
		joined="tempJoined_1"
	else
		joined="joined"
	fi
	join -a1 -a2 -1 2 -2 2 -o 0 1.1 2.1 -e "0" ${names[0]}"_ppr_sorted_first.txt" ${names[1]}"_ppr_sorted_first.txt" > $joined".txt"
	finalLoop=`expr ${#names[@]} - 1`
	columns="1.2"
	if [ ${#names[@]} -gt  2 ] ;
	then
	  for i in $(seq 2 $finalLoop);
	  do
		echo ${names[$i]}
		currentName=${names[$i]}
		currentColumn=`expr $i + 1`
		columns=$columns" 1."$currentColumn
		if [ "$i" -eq "$finalLoop" ] ;
		then
			joinedNew="joined" #final file should be named joined.txt
		else
			joinedNew=$joined"_"$i #temp name of file otherwise
		fi
		cmd="join -a1 -a2 -1 1 -2 2 -o 0 "$columns" 2.1 -e "0" "$joined".txt "$currentName"_ppr_sorted_first.txt > "$joinedNew".txt"			
		eval $cmd
		joined=$joinedNew
	  done
	fi
else
	awk '{ print $2 " " $1}' ${names[0]}"_ppr_sorted_first.txt" > "joined.txt"
fi
