#!/usr/bin/env python
#encoding=utf-8

import commands;

chrs = [
    'chr1',
    'chr10',
    'chr11',
    'chr12',
    'chr13',
    'chr14',
    'chr15',
    'chr16',
    'chr17',
    'chr18',
    'chr19',
    'chr2',
    'chr20',
    'chr21',
    'chr22',
    'chr3',
    'chr4',
    'chr5',
    'chr6',
    'chr7',
    'chr8',
    'chr9',
    'chrX',
    'chrY'    
];

def main():
    
    foRun = open('run.sh', 'w');
    foSubmit = open('submit.sh', 'w');
    
    for chromo in chrs:
        shFile = '/ifs4/ISDC_BD/xiaopeng2/src/DHGV/script/BGI-Psorasis/unify/unify.' + chromo + '.mapred.sh';
        fo = open(shFile, 'w');
        fo.write('#!/bin/bash' + "\n");
        fo.write('HADOOP="/usr/bin/hadoop"' + "\n");
        fo.write('STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"' + "\n");
        fo.write('NAME="' + chromo + '"' + "\n");
        fo.write('INPUT="/user/xiaopeng2/DHGV/input/bgi.psoriasis"' + "\n");
        fo.write('OUTPUT="/user/xiaopeng2/DHGV/unify/bgi.psoriasis/$NAME/output"' + "\n");
        fo.write('MAPPER="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/UnifyMapper.py"' + "\n");
        fo.write('REDUCER="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/UnifyBGIPsorasis.py"' + "\n");
        fo.write('$HADOOP fs -rm -r -skipTrash $OUTPUT' + "\n");
        fo.write('time -p $HADOOP jar $STREAMING_JAR -D mapreduce.job.name="DHGV.BGI-Psorasis.$NAME.unify" -D stream.num.map.output.key.fields=2 -D mapreduce.job.reduces=149 -output $OUTPUT -mapper "$MAPPER $NAME" -reducer $REDUCER -file $MAPPER -file $REDUCER -input $INPUT 1>$0.o 2>$0.e' + "\n");
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