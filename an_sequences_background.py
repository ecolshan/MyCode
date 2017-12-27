#!/home/wuq/tools/python-2.7.3/bin/python
import os,re
from Bio import AlignIO
os.system('date')
if len(os.sys.argv) != 3: exit('''Usage: /home/wuq/projects/convergence/an_sequences 0 100''')
x = int(os.sys.argv[1])
y = int(os.sys.argv[2])
codeml_ctl = ''
for n in open('/home/wuq/projects/convergence/bin/codeml.ctl'):
    codeml_ctl += n
for i in range(x,y):
    f = 'family_'+str(i).zfill(5)
    os.chdir('/home/wuq/projects/convergence/workShop_background/'+f+'/rst/')
    alignments = list(AlignIO.parse('/home/wuq/projects/convergence/workShop_background/'+f+'/aln/'+f+'.phy', "phylip"))
    all = {}
    for num in xrange(0,len(alignments[0][0].seq)):
        fas = ''
        codeml_change = ''
        an_seq = ''
        for n in alignments[0]:
            fas += '>' + n.id + '\n' + str(n.seq)[num] + '\n'
            all[n.id[:3]] = str(n.seq)[num]
        if all['aml'] == all['mpu'] and all['aml'] != all['pbe'] and all['afu'] != all['mpu'] and all['aml'] != '-' and all['afu'] != '-' and all['pbe'] != '-' and all['mpu'] != '-':
            fh_2 = open('/home/wuq/projects/convergence/workShop_background/'+f+'/rst/'+str(num)+'.faa','w')
            fh_2.write(fas)
            fh_2.close()  
            fh_1 = open('/home/wuq/projects/convergence/workShop_background/'+f+'/rst/codeml.ctl','w')
            codeml_change += 'seqfile = /home/wuq/projects/convergence/workShop_background/'+f+'/rst/'+str(num)+'.faa'+'\n'+'outfile = /home/wuq/projects/convergence/workShop_background/'+f+'/rst/'+str(num)+'_sites_mlc\n'+'treefile = /home/wuq/projects/convergence/bin/H0_3.tree'+'\n'+codeml_ctl[209:]
            fh_1.write(codeml_change)
            fh_1.close()
            os.system('/home/wuq/projects/convergence/bin/codeml /home/wuq/projects/convergence/workShop_background/'+f+'/rst/codeml.ctl')
            fh_3 = open('/home/wuq/projects/convergence/workShop_background/'+f+'/rst/rst_'+str(num)+'.txt','w')
            for line in open('/home/wuq/projects/convergence/workShop_background/'+f+'/rst/rst','r'):
                an_seq += line
            fh_3.write(an_seq)
            fh_3.close()
            print f
            os.system('rm /home/wuq/projects/convergence/workShop_background/'+f+'/rst/rub')
            os.system('rm /home/wuq/projects/convergence/workShop_background/'+f+'/rst/rst')
            os.system('rm /home/wuq/projects/convergence/workShop_background/'+f+'/rst/rst1')
            os.system('rm /home/wuq/projects/convergence/workShop_background/'+f+'/rst/lnf')
            os.system('rm /home/wuq/projects/convergence/workShop_background/'+f+'/rst/codeml.ctl')   
os.system('date')    
