#!/bin/bash
IN_SUFFIX=".fasta"
echo 'set data dir'
DATADIR=$1 
OUTDIR=$2 
mkdir $OUTDIR
cd $DATADIR
for FILE_NAME in *$IN_SUFFIX	
do 
(	
	echo 'run script'$FILE_NAME
	IN_NAME=${FILE_NAME%.*}
	echo $IN_NAME
	"/root/scripts/scripts_trf/trf407b.linux64" $IN_NAME$IN_SUFFIX 2 7 7 80 10 50 15 -h -ngs > $OUTDIR"/"$IN_NAME".out"
)&
done
wait

