#!/user/bin/env python

import json;
import sys;

def main():
    
    for line in sys.stdin:
        line = line.strip();
        if line == '':
            continue;
        
        data = json.loads(line);
        pvfd = [];
        classes = ['overall', 'source', 'ethnicity', 'country', 'province', 'age', 'gender'];
        
        # HBASE_ROW_KEY
        # data:rs_ids
        # data:ref
        # data:alts
        # data:sample_count
        # data:total_read_depth
        # data:avg_read_depth
        # data:create_ts
        # data:update_ts
        # data:overall
        # data:source
        # data:ethnicity
        # data:country
        # data:province
        # data:age
        # data:gender
        rowKey = data.get('referenceName') + '-' + str(data.get('start'));
        rsIDs = ','.join(data.get('variantNames'));
        ref = data.get('referenceBases');
        alts = ','.join(data.get('alternativeBases'));
        sampleCount = str(data.get('totalCallSetCount'));
        totalReadDepth = str(data.get('totalReadDepth'));
        avgReadDepth = str(data.get('avgReadDepth'));
        createTs = str(data.get('created'));
        updateTs = str(data.get('updated'));
        
        pvfd.append(rowKey);
        pvfd.append(rsIDs);
        pvfd.append(ref);
        pvfd.append(alts);
        pvfd.append(sampleCount);
        pvfd.append(totalReadDepth);
        pvfd.append(avgReadDepth);
        pvfd.append(createTs);
        pvfd.append(updateTs);
        
        for cls in classes:
            pvfd.append(json.dumps(data.get(cls), ensure_ascii = False));
    
        print "\t".join(pvfd);
    
    pass;

if __name__ == '__main__':
    main();