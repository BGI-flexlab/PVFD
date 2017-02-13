#!/usr/bin/env python
#encoding=utf-8

import commands;

data = {
    'chr1' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr1.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr2' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr2.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr3' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr3.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr4' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr4.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr5' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr5.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr6' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr6.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr7' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr7.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr8' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr8.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr9' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr9.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr10' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr10.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr11' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr11.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr12' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr12.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr13' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr13.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr14' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr14.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr15' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr15.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr16' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr16.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr17' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr17.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr18' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr18.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr19' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr19.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr20' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr20.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr21' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr21.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chr22' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz',
    'chrX' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.vcf.gz',
    'chrY' : '/ifs4/ISDC_BD/xiaopeng2/database/1000Genomes/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.vcf.gz' 
};

def main():
    
    foRun = open('run.sh', 'w');
    foSubmit = open('submit.sh', 'w');
    
    for chromo in data.keys():
        fo = open('/ifs4/ISDC_BD/xiaopeng2/src/DHGV/script/run1kg.vcf2json.' + chromo + '.mapred.sh', 'w');
        fo.write('#!/bin/bash' + "\n");
        fo.write('HADOOP="/usr/bin/hadoop"' + "\n");
        fo.write('STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"' + "\n");
        fo.write('NAME="' + chromo + '"' + "\n");
        fo.write('INPUT="file://' + data.get(chromo) + '"' + "\n");
        fo.write('OUTPUT="/user/xiaopeng2/DHGV/vcf2json/1000Genomes/$NAME/output"' + "\n");
        fo.write('FILE="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/t1kg.vcf2json.py"' + "\n");
        fo.write('$HADOOP fs -rm -r -skipTrash $OUTPUT' + "\n");
        fo.write('time -p $HADOOP jar $STREAMING_JAR -D mapreduce.job.name="DHGV.1000Genomes.$NAME.vcf2json" -D stream.num.map.output.key.fields=2 -D mapreduce.job.reduces=159 -output $OUTPUT -mapper "/bin/cat" -reducer $FILE -file $FILE -input $INPUT 1>$0.o 2>$0.e' + "\n");
        fo.close();
        
        if chromo != 'chrY':
            foRun.write("sh /ifs4/ISDC_BD/xiaopeng2/src/DHGV/script/run1kg.vcf2json." + chromo + '.mapred.sh' + "\n");
        
    foSubmit.write('nohup time -p sh run.sh 1>$0.o 2>$0.e &');
    
    foRun.close();
    foSubmit.close();
    
    (status, output) = commands.getstatusoutput("chmod 750 *.sh");
    
    pass;

if __name__ == '__main__':
    main();