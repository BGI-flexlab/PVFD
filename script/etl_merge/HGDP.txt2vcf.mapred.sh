#!/bin/bash
HADOOP="/usr/bin/hadoop"
STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"
INPUT="file:///ifs4/ISDC_BD/xiaopeng2/src/DHGV/data/hgdp/HGDP_FinalReport_Forward.txt"
OUTPUT="/user/xiaopeng2/DHGV/txt2vcf/HGDP/output"
FILE="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/HGDP.txt2vcf.py"
$HADOOP fs -rm -r -skipTrash $OUTPUT
nohup time -p $HADOOP jar $STREAMING_JAR -D mapreduce.job.name="HGDP.txt2vcf" -D stream.num.map.output.key.fields=2 -D mapreduce.job.reduces=149 -output $OUTPUT -mapper "/bin/cat" -reducer $FILE -file $FILE -input $INPUT 1>$0.o 2>$0.e &