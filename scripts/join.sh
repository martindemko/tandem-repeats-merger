#!/bin/bash
#joins files in folder $1 together, in order defined in names. The files were previously sorted by createTable.sh
if  [[ "$2" = /* ]]; then
	DATADIR="$2"
else
	DATADIR="$PWD/$2"
fi
if  [[ "$1" = /* ]]; then
	WORKDIR="$1"
else
	WORKDIR="$PWD/$1"
fi
ind=0
#for name in "${DATADIR}/*"
#do
#	names[ind]="`basename ${name%.*}`"
#	((ind++))
#done

cd "$DATADIR"
for name in *
do
	names[ind]="${name%.*}"
	((ind++))
done

cd "$WORKDIR"
for i in ${!names[@]}
do

if [ ${i} -gt 0 ] ;
then
	COMMAND="${COMMAND} | join -a1 -a2 -e0 -o auto - <(awk '{print \$2\" \"\$1}' \"${names[$i]}_ppr_sorted.txt\")"
else
	COMMAND="awk '{ print \$2\" \"\$1}' \"${names[$i]}_ppr_sorted.txt\""
fi

done

COMMAND="$COMMAND > joined.txt"

echo "COMMAND: $COMMAND"
eval $COMMAND
