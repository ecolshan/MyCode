#!/home/wuq/tools/python-2.7.3/bin/python
import os,re
os.system('date')
fh = open('/home/wuq/projects/convergence/an_research_background.txt','w')
for family in os.listdir('/home/wuq/projects/convergence/workShop_background/'):
    for rst in os.listdir('/home/wuq/projects/convergence/workShop_background/'+family+'/rst/'):
        an = ''
        if rst[-4:] == '.txt':
            for line in open('/home/wuq/projects/convergence/workShop_background/'+family+'/rst/'+rst):
                an += line
            #print family,rst,an;raw_input()
            faa_id = rst.split('.')[0].split('_')[1]
            giant = re.findall('aml|panda_[\s]+(.+)',an)[4]
            red = re.findall('afu|red-pa[\s]+(.+)',an)[4]
            pbe = re.findall('pbe|Uma_R0[\s]+(.+)',an)[4]
            mpu = re.findall('mpu|ENSMPU[\s]+(.+)',an)[4]
            caf = re.findall('caf|ENSCAF[\s]+(.+)',an)[4]
            tig = re.findall('tig|PTIG00[\s]+(.+)',an)[4]
            hum = re.findall('hum|ENSP00[\s]+(.+)',an)[4]
            mus = re.findall('mus|ENSMUS[\s]+(.+)',an)[4]
            an_giant = re.findall('#13[\s]+(.+)',an)[0]
            an_mpu = re.findall('#14[\s]+(.+)',an)[0]
            if giant == mpu and giant != red and mpu != pbe and giant != an_giant and mpu != an_mpu:
             # print family,'\t',faa_id,'\t',an_giant,an_red,'\t',giant,red,pbe,mpu,caf,tig,hum,mus;raw_input()
               fh.write(family+'\t'+faa_id+'\t'+an_giant+an_mpu+'\t'+giant+mpu+pbe+red+caf+tig+hum+mus+'\n')
fh.close()
os.system('date')

