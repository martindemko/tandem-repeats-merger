#!/bin/bash

#echo 'set data dir'
IN_SUFFIX=".fasta"
DATADIR="$1"
OUTDIR="$2"
trf_match="$3"   # matching weight
trf_mism="$4"    # mismatching penalty
trf_delta="$5"   # indel penalty
trf_pm="$6"     # match probability (whole number)
trf_pi="$7"     # indel probability (whole number)
trf_min="$8"    # minimum alignment score to report
trf_max="$9"    # maximum period size to report
trf_longest="${10}"	# longest length of TR array
trf_html="${11}"	# if you want also HTML output from TRF
TOOL="`which trf`"
N="${GALAXY_SLOTS:-1}"
mkdir "$OUTDIR"
(
for FILE_NAME in "${DATADIR}"/*
do
	((i=i%N)); ((i++==0)) && wait
	IN_NAME="${FILE_NAME%.*}"
	IN_FILE="${IN_NAME}${IN_SUFFIX}"
	mv "$FILE_NAME" "$IN_FILE"
	OUT_FILE="${OUTDIR}/`basename ${IN_NAME}`.dat"
	echo "run TRF for ${FILE_NAME} into ${OUT_FILE}"
	echo "${TOOL} $IN_FILE $trf_match $trf_mism $trf_delta $trf_pm $trf_pi $trf_min $trf_max -l $trf_longest $trf_html -ngs > ${OUT_FILE} &"
	"${TOOL}" "$IN_FILE" "$trf_match" "$trf_mism" "$trf_delta" "$trf_pm" "$trf_pi" "$trf_min" "$trf_max" -l "$trf_longest" "$trf_html" -ngs > "${OUT_FILE}" &
done
wait
)

