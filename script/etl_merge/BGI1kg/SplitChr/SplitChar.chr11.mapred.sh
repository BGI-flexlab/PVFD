#!/bin/bash
HADOOP="/usr/bin/hadoop"
STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"
NAME="chr11"
INPUT="/user/xiaopeng2/DHGV/unify/BGI1000G/output"
OUTPUT="/user/xiaopeng2/DHGV/unify/BGI1000G/$NAME"
FILE="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/SplitChrMapper.py"
$HADOOP fs -rm -r -skipTrash $OUTPUT
time -p $HADOOP jar $STREAMING_JAR -D mapreduce.job.name="DHGV.BGI1000G.$NAME.SplitChr" -D stream.num.map.output.key.fields=2 -D mapreduce.job.reduces=149 -output $OUTPUT -mapper "$FILE $NAME" -file $FILE -input $INPUT 1>$0.o 2>$0.e
