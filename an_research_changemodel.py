#!/home/wuq/tools/python-2.7.3/bin/python
import os,re
os.system('date')
fh = open('/home/wuq/projects/convergence/an_research_changdemodel.txt','w')
for family in os.listdir('/home/wuq/projects/convergence/workShop_14254_changemodel/'):
    for rst in os.listdir('/home/wuq/projects/convergence/workShop_14254_changemodel/'+family+'/rst/'):
        an = ''
        if rst[-4:] == '.txt' and rst[:3] == 'rst':
            #print rst;raw_input()
            for line in open('/home/wuq/projects/convergence/workShop_14254_changemodel/'+family+'/rst/'+rst):
                an += line
            #print family
            faa_id = rst.split('.')[0].split('_')[1]
            #print re.findall('aml|panda_[\s]+(.+)',an);raw_input()
            giant = re.findall('aml|panda_[\s]+(.+)',an)[4]
            red = re.findall('afu|red-pa[\s]+(.+)',an)[4]
            pbe = re.findall('pbe|Uma_R0[\s]+(.+)',an)[4]
            mpu = re.findall('mpu|ENSMPU[\s]+(.+)',an)[4]
            caf = re.findall('caf|ENSCAF[\s]+(.+)',an)[4]
            tig = re.findall('tig|PTIG00[\s]+(.+)',an)[4]
            hum = re.findall('hum|ENSP00[\s]+(.+)',an)[4]
            mus = re.findall('mus|ENSMUS[\s]+(.+)',an)[4]
            an_giant = re.findall('#13[\s]+(.+)',an)[0] 
            an_red = re.findall('#14[\s]+(.+)',an)[0]
            if giant == red and giant != pbe and red != mpu and giant != an_giant and red != an_red :
             # print family,'\t',faa_id,'\t',an_giant,an_red,'\t',giant,red,pbe,mpu,caf,tig,hum,mus;raw_input() 
               fh.write(family+'\t'+faa_id+'\t'+an_giant+an_red+'\t'+giant+red+pbe+mpu+caf+tig+hum+mus+'\n')
fh.close()
os.system('date')    
