#!/bin/bash
HADOOP="/usr/bin/hadoop"
STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"
INPUT="/user/xiaopeng2/DHGV/input/bgi.1kg"
OUTPUT="/user/xiaopeng2/DHGV/unify/BGI1000G/output"
FILE="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/UnifyMapper.py"
$HADOOP fs -rm -r -skipTrash $OUTPUT
nohup time -p $HADOOP jar $STREAMING_JAR -D mapreduce.job.name="BGI1000G.UniqueChrs" -D stream.num.map.output.key.fields=2 -D mapreduce.job.reduces=149 -output $OUTPUT -mapper $FILE -reducer "/bin/cat" -file $FILE -input $INPUT 1>$0.o 2>$0.e &