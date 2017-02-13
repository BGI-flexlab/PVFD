#!/bin/bash
HADOOP="/usr/bin/hadoop"
STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"
INPUT="file:///lfs1/ISDC_BD/data/Variants/bgi.1kg/*.vcf"
OUTPUT="/user/xiaopeng2/DHGV/vcf2vcf/BGI1kg/output"
FILE="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/BGI1kg.vcf2vcf.py"
$HADOOP fs -rm -r -skipTrash $OUTPUT
nohup time -p $HADOOP jar $STREAMING_JAR -D mapreduce.job.name="DHGV.BGI1kg.vcf2vcf" -D stream.num.map.output.key.fields=2 -D mapreduce.job.reduces=149 -output $OUTPUT -mapper "/bin/cat" -reducer $FILE -file $FILE -input $INPUT 1>$0.o 2>$0.e &
