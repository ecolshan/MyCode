#!/home/wuq/tools/python-2.7.3/bin/python
import os,re
from Bio import AlignIO
os.system('date')
if len(os.sys.argv) != 3: exit('''Usage: /home/wuq/projects/convergence/an_sequences 0 100''')
x = int(os.sys.argv[1])
y = int(os.sys.argv[2])
codeml_ctl = ''
for n in open('/home/wuq/projects/convergence/bin/codeml_cm.ctl'):
    codeml_ctl += n
#print codeml_ctl[209:]
for i in range(x,y):
    f = 'family_'+str(i).zfill(5)
    os.chdir('/home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/')
    alignments = list(AlignIO.parse('/home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/aln/'+f+'.phy', "phylip"))
    all = {}
    for num in xrange(0,len(alignments[0][0].seq)):
        fas = ''
        codeml_change = ''
        an_seq = ''
        rates = ''
        for n in alignments[0]:
            fas += '>' + n.id + '\n' + str(n.seq)[num] + '\n'
            all[n.id[:3]] = str(n.seq)[num]
        aaCheck = {}
        for j,k in all.items():
            if k == '-': continue
            if aaCheck.has_key(k):  aaCheck[k] += 1
            else:  aaCheck[k] = 1
        if all['aml'] == all['afu']  and all['aml'] != '-' and all['afu'] != '-' and all['pbe'] != '-' and len(aaCheck) >= 2:
            fh_2 = open('/home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/'+str(num)+'.faa','w')
            fh_2.write(fas)
            fh_2.close()  
            fh_1 = open('/home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/codeml_cm.ctl','w')
            codeml_change += 'seqfile = /home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/'+str(num)+'.faa'+'\n'+'outfile = /home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/'+str(num)+'_sites_mlc\n'+'treefile = /home/wuq/projects/convergence/bin/H0_3_unrooted.tree'+'\n'+codeml_ctl[209:]
            fh_1.write(codeml_change)
            fh_1.close()
            os.system('/home/wuq/projects/convergence/bin/codeml /home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/codeml_cm.ctl')
            fh_3 = open('/home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/rst_'+str(num)+'.txt','w')
            for line in open('/home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/rst','r'):
                an_seq += line
            fh_3.write(an_seq)
            fh_3.close()
            fh_4 = open('/home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/rates_'+str(num)+'.txt','w')
            for line_2 in open('/home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/rates','r'):
                rates += line_2
            fh_4.write(rates)
            fh_4.close()
            print f
            os.system('rm /home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/rub')
            os.system('rm /home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/rst')
            os.system('rm /home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/rst1')
            os.system('rm /home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/lnf')
            os.system('rm /home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/codeml_cm.ctl')   
            os.system('rm /home/wuq/projects/convergence/workShop_14254_zjz/'+f+'/rst/rates')
os.system('date')    
