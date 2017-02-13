#!/bin/bash
HADOOP="/usr/bin/hadoop"
STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"
INPUT="file:///ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz"
OUTPUT="/user/xiaopeng2/DHGV/vcf2json/output"
FILE="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/t1kg.vcf2json.py"
$HADOOP fs -rm -r -skipTrash $OUTPUT
nohup time -p $HADOOP jar $STREAMING_JAR -D mapreduce.job.name="DHGV.1000Genomes.chr22.vcf2json" -D stream.num.map.output.key.fields=2 -D mapreduce.job.reduces=159 -output $OUTPUT -mapper "/bin/cat" -reducer $FILE -file $FILE -input $INPUT 1>$0.o 2>$0.e &