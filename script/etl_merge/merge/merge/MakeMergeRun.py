#!/usr/bin/env python
#encoding=utf-8

import commands;

_T1000G_Chrs = ['chr1', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr20', 'chr21', 'chr22', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chrX', 'chrY'];
_HGDP_Chrs = ['chr1', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr20', 'chr21', 'chr22', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chrX', 'chrY', 'chrM'];
_EGP95_Chrs = [
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
    'chrGL000191.1',
    'chrGL000192.1',
    'chrGL000193.1',
    'chrGL000194.1',
    'chrGL000195.1',
    'chrGL000196.1',
    'chrGL000197.1',
    'chrGL000198.1',
    'chrGL000199.1',
    'chrGL000201.1',
    'chrGL000202.1',
    'chrGL000203.1',
    'chrGL000204.1',
    'chrGL000205.1',
    'chrGL000206.1',
    'chrGL000207.1',
    'chrGL000208.1',
    'chrGL000209.1',
    'chrGL000210.1',
    'chrGL000211.1',
    'chrGL000212.1',
    'chrGL000213.1',
    'chrGL000214.1',
    'chrGL000215.1',
    'chrGL000216.1',
    'chrGL000217.1',
    'chrGL000218.1',
    'chrGL000219.1',
    'chrGL000220.1',
    'chrGL000221.1',
    'chrGL000222.1',
    'chrGL000223.1',
    'chrGL000224.1',
    'chrGL000225.1',
    'chrGL000226.1',
    'chrGL000227.1',
    'chrGL000228.1',
    'chrGL000229.1',
    'chrGL000230.1',
    'chrGL000231.1',
    'chrGL000232.1',
    'chrGL000233.1',
    'chrGL000234.1',
    'chrGL000235.1',
    'chrGL000236.1',
    'chrGL000237.1',
    'chrGL000238.1',
    'chrGL000239.1',
    'chrGL000240.1',
    'chrGL000241.1',
    'chrGL000242.1',
    'chrGL000243.1',
    'chrGL000244.1',
    'chrGL000245.1',
    'chrGL000246.1',
    'chrGL000247.1',
    'chrGL000248.1',
    'chrGL000249.1',
    'chrMT',
    'chrNC_007605',
    'chrX',
    'chrY'    
];
_ESP6500_Chrs = ['chr1', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr20', 'chr21', 'chr22', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chrX', 'chrY'];
_BGI1000G_Chrs = ['chr1', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr20', 'chr21', 'chr22', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chrX', 'chrY'];
_BGIPsorasis_Chrs = ['chr1', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr20', 'chr21', 'chr22', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chrX', 'chrY'];

_T1000G_Dir = '/user/xiaopeng2/DHGV/unify/1000Genomes/';
_HGDP_Dir = 'file:///ifs4/ISDC_BD/xiaopeng2/src/DHGV/data/variation/HGDP/';
_EGP95_Dir = '/user/xiaopeng2/DHGV/unify/EGP95/';
_ESP6500_Dir = 'file:///ifs4/ISDC_BD/xiaopeng2/src/DHGV/data/variation/ESP6500/';
_BGI1000G_Dir = '/user/xiaopeng2/DHGV/unify/BGI1000G/';
_BGIPsorasis_Dir = '/user/xiaopeng2/DHGV/unify/bgi.psoriasis/';

def main():
    
    foRun = open('run.sh', 'w');
    foSubmit = open('submit.sh', 'w');
    
    chrs = [];
    for chromo in _T1000G_Chrs:
        if chromo not in chrs:
            chrs.append(chromo);    
    
    for chromo in _HGDP_Chrs:
        if chromo not in chrs:
            chrs.append(chromo);
    
    for chromo in _EGP95_Chrs:
        if chromo not in chrs:
            chrs.append(chromo);
    
    for chromo in _ESP6500_Chrs:
        if chromo not in chrs:
            chrs.append(chromo);
    
    for chromo in _BGI1000G_Chrs:
        if chromo not in chrs:
            chrs.append(chromo);
            
    for chromo in _BGIPsorasis_Chrs:
        if chromo not in chrs:
            chrs.append(chromo);
    
    
    for chromo in sorted(chrs):
        
        inputs = [];
        
        if chromo in _T1000G_Chrs:
            inputs.append(_T1000G_Dir + chromo + '/output');
            
        if chromo in _HGDP_Chrs:
            inputs.append(_HGDP_Dir + chromo + '.tsv');
            
        if chromo in _EGP95_Chrs:
            inputs.append(_EGP95_Dir + chromo + '/output');
            
        if chromo in _ESP6500_Chrs:
            inputs.append(_ESP6500_Dir + chromo + '.tsv');
            
        if chromo in _BGI1000G_Chrs:
            inputs.append(_BGI1000G_Dir + chromo);
            
        if chromo in _BGIPsorasis_Chrs:
            inputs.append(_BGIPsorasis_Dir + chromo + '/output');
        
        shFile = '/ifs4/ISDC_BD/xiaopeng2/src/DHGV/script/merge/merge/merge.' + chromo + '.mapred.sh';
        fo = open(shFile, 'w');
        fo.write('#!/bin/bash' + "\n");
        fo.write('HADOOP="/usr/bin/hadoop"' + "\n");
        fo.write('STREAMING_JAR="/ifs4/ISDC_BD/software/hadoop/CDH/CDH5/5.6.0/hadoop-streaming-2.6.0-cdh5.6.0.jar"' + "\n");
        fo.write('NAME="' + chromo + '"' + "\n");
        fo.write('OUTPUT="/user/xiaopeng2/DHGV/merge/merge/$NAME"' + "\n");
        fo.write('FILE="/ifs4/ISDC_BD/xiaopeng2/src/DHGV/etl/Merge.Tsv2Json.py"' + "\n");
        fo.write('$HADOOP fs -rm -r -skipTrash $OUTPUT' + "\n");
        fo.write('time -p $HADOOP jar $STREAMING_JAR -D mapreduce.job.name="DHGV.$NAME.merge" -D stream.num.map.output.key.fields=2 -D mapreduce.job.reduces=149 -output $OUTPUT -mapper "/bin/cat" -reducer $FILE -file $FILE -input ' + ' -input '.join(inputs) + ' 1>$0.o 2>$0.e' + "\n");
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