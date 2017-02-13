#!/bin/bash
HADOOP="/usr/bin/hadoop"
STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"
INPUT1_chr1="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr1/output"
INPUT1_chr2="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr2/output"
INPUT1_chr3="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr3/output"
INPUT1_chr4="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr4/output"
INPUT1_chr5="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr5/output"
INPUT1_chr6="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr6/output"
INPUT1_chr7="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr7/output"
INPUT1_chr8="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr8/output"
INPUT1_chr9="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr9/output"
INPUT1_chr10="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr10/output"
INPUT1_chr11="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr11/output"
INPUT1_chr12="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr12/output"
INPUT1_chr13="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr13/output"
INPUT1_chr14="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr14/output"
INPUT1_chr15="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr15/output"
INPUT1_chr16="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr16/output"
INPUT1_chr17="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr17/output"
INPUT1_chr18="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr18/output"
INPUT1_chr19="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr19/output"
INPUT1_chr20="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr20/output"
INPUT1_chr21="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr21/output"
INPUT1_chr22="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chr22/output"
INPUT1_chrX="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chrX/output"
INPUT1_chrY="/user/xiaopeng2/DHGV/vcf2vcf/1000Genomes/chrY/output"
INPUT2="file:///ifs4/ISDC_BD/xiaopeng2/src/DHGV/data/HGDP.unique_variants.vcf"
INPUT3="/user/xiaopeng2/DHGV/vcf2vcf/NIEHS/output"
INPUT4="/user/xiaopeng2/DHGV/vcf2vcf/NHLBI/output"
INPUT5="/user/xiaopeng2/DHGV/vcf2vcf/BGI1kg/output"
OUTPUT="/user/xiaopeng2/DHGV/vcf2vcf/merge/output"
FILE="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/merge.vcf2vcf.py"
$HADOOP fs -rm -r -skipTrash $OUTPUT
nohup time -p $HADOOP jar $STREAMING_JAR \
    -D mapreduce.job.name="DHGV.merge.vcf2vcf" \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.job.reduces=149 \
    -output $OUTPUT \
    -mapper "/bin/cat" \
    -reducer $FILE \
    -file $FILE \
    -input $INPUT1_chr1 \
    -input $INPUT1_chr2 \
    -input $INPUT1_chr3 \
    -input $INPUT1_chr4 \
    -input $INPUT1_chr5 \
    -input $INPUT1_chr6 \
    -input $INPUT1_chr7 \
    -input $INPUT1_chr8 \
    -input $INPUT1_chr9 \
    -input $INPUT1_chr10 \
    -input $INPUT1_chr11 \
    -input $INPUT1_chr12 \
    -input $INPUT1_chr13 \
    -input $INPUT1_chr14 \
    -input $INPUT1_chr15 \
    -input $INPUT1_chr16 \
    -input $INPUT1_chr17 \
    -input $INPUT1_chr18 \
    -input $INPUT1_chr19 \
    -input $INPUT1_chr20 \
    -input $INPUT1_chr21 \
    -input $INPUT1_chr22 \
    -input $INPUT1_chrX \
    -input $INPUT1_chrY \
    -input $INPUT2 \
    -input $INPUT3 \
    -input $INPUT4 \
    -input $INPUT5 1>$0.o 2>$0.e &