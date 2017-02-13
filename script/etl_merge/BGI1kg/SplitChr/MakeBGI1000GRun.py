#!/usr/bin/env python
#encoding=utf-8

import commands;

data = {
    'chr1' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr1.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr2' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr2.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr3' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr3.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr4' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr4.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr5' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr5.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr6' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr6.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr7' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr7.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr8' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr8.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr9' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr9.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr10' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr10.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr11' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr11.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr12' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr12.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr13' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr13.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr14' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr14.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr15' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr15.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr16' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr16.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr17' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr17.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr18' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr18.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr19' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr19.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr20' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr20.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr21' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr21.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr22' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf',
    'chrX' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.vcf.gz',
    'chrY' : '/user/xiaopeng2/DHGV/input/1000Genomes/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.vcf' 
};

def main():
    
    foRun = open('run.sh', 'w');
    foSubmit = open('submit.sh', 'w');
    
    for chromo in data.keys():
        shFile = '/ifs4/ISDC_BD/xiaopeng2/src/DHGV/script/BGI1kg/SplitChr/SplitChar.' + chromo + '.mapred.sh';
        fo = open(shFile, 'w');
        fo.write('#!/bin/bash' + "\n");
        fo.write('HADOOP="/usr/bin/hadoop"' + "\n");
        fo.write('STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"' + "\n");
        fo.write('NAME="' + chromo + '"' + "\n");
        fo.write('INPUT="/user/xiaopeng2/DHGV/unify/BGI1000G/output"' + "\n");
        fo.write('OUTPUT="/user/xiaopeng2/DHGV/unify/BGI1000G/$NAME"' + "\n");
        fo.write('FILE="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/SplitChrMapper.py"' + "\n");
        fo.write('$HADOOP fs -rm -r -skipTrash $OUTPUT' + "\n");
        fo.write('time -p $HADOOP jar $STREAMING_JAR -D mapreduce.job.name="DHGV.BGI1000G.$NAME.SplitChr" -D stream.num.map.output.key.fields=2 -D mapreduce.job.reduces=149 -output $OUTPUT -mapper "$FILE $NAME" -file $FILE -input $INPUT 1>$0.o 2>$0.e' + "\n");
        fo.close();
        
        # if chromo != 'chrY':
        #     foRun.write("sh " + shFile + "\n");
        foRun.write("sh " + shFile + "\n");
        
    foSubmit.write('nohup time -p sh run.sh 1>$0.o 2>$0.e &');
    
    foRun.close();
    foSubmit.close();
    
    (status, output) = commands.getstatusoutput("chmod 750 *.sh");
    
    pass;

if __name__ == '__main__':
    main();