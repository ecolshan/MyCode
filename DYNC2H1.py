#!/usr/bin/env python
import os
all = {'>afu|red-pa_ENSP00000381167':'','>hum|ENSP00000381167':'','>aml|panda_ENSP00000381167':'','>caf|ENSCAF_ENSP00000381167':'','>tig|PTIG00_ENSP00000381167':'','>pbe|Uma_R0_ENSP00000381167':'','>mus|ENSMUS_ENSP00000381167':'','>mpu|ENSMPU_ENSP00000381167':''}
count =0
fh = open('DYNC2H1.faa','w')
for i in open('DYNC2H1.fas','r'):
    count += 1
    if count != 1 :
       seq = i.split('\t')
       num = 0
       for n in seq :
           num += 1
           if num == 2 : all['>hum|ENSP00000381167'] += n
           elif num == 3 : all['>pbe|Uma_R0_ENSP00000381167'] += n
           elif num == 4 : all['>afu|red-pa_ENSP00000381167'] += n
           elif num == 5 : all['>tig|PTIG00_ENSP00000381167'] += n
           elif num == 6 : all['>aml|panda_ENSP00000381167'] += n
           elif num == 7 : all['>caf|ENSCAF_ENSP00000381167'] += n
           elif num == 8 : all['>mpu|ENSMPU_ENSP00000381167'] += n
           elif num == 9 : all['>mus|ENSMUS_ENSP00000381167'] += n.strip()
     #  print all;raw_input()
for sp,seq in all.items():
    fh.write(sp+'\n'+seq+'\n')
fh.close()
