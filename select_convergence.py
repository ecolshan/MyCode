#!/home/wuq/tools/python-2.7.3/bin/python
import os
from Bio import AlignIO
#fh = open('/home/wuq/projects/convergence/select_convergence.txt','w')
fh = open('/home/wuq/projects/convergence/select_convergence_6.txt','w')
for family in os.listdir('/home/wuq/projects/convergence/workShop_14254/'):
    alignments = list(AlignIO.parse('/home/wuq/projects/convergence/workShop_14254/'+family+'/aln/'+family+'.phy', "phylip"))
    all = {}
    for i in xrange(0,len(alignments[0][0].seq)):
        fas = ''
        for x in alignments[0]:
            fas += '>' + x.id + '\n' + str(x.seq)[i] + '\n'
            all[x.id[:3]] = str(x.seq)[i]
       # if all['aml'] == all['afu'] and all['aml'] != all['pbe'] and all['aml'] != all['mpu'] and all['aml'] != all['caf'] and all['aml'] != all['tig'] and all['aml'] != all['hum'] and all['aml'] != all['mus'] :
        if all['aml'] == all['afu'] and all['aml'] != all['pbe'] and all['aml'] != all['mpu'] and all['aml'] != all['caf'] and all['aml'] != all['tig'] :
           fh.write(family+'\t'+str(i)+'\t'+str(all)+'\n')
fh.close()
        
