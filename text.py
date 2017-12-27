#!/usr/bin/env python
import os,re
count = 0
a = ''
o = ''
b = ''
all_A = {}
all_B = {
    'afu|red-pa':'',
    'aml|ENSAME':'',
    'caf|ENSCAF':'',
    'pbe|scaffo':'',
    'mpu|ENSMPU':'',
}

key = 'afu|red-pa,aml|ENSAME,caf|ENSCAF,pbe|scaffo,mpu|ENSMPU'
for line in open ('/home/wuq/projects/convergence/workShop_3/family_3516/sites/242.faa'):
    count += 1
    if (count%2) == 1:
       a += line[:-1]
    if (count%2) == 0:
       o += line[:-1]
    j = a.split('>')[1:]
print j;raw_input()
for i in range (0,8):
    all_A[j[i]]=o[i]
print all_A,all_B;raw_input()
for k in all_B.keys():
    all_B[k] = all_A[k]
for j in all_B.values():
    b += j
    x = set(b)
print all_A,'\n',all_B,'\n',x
if len(x) == 2 and all_A['afu|red-pa'] == all_A['aml|ENSAME'] and all_A['caf|ENSCAF'] == all_A['pbe|scaffo'] == all_A['mpu|ENSMPU']:
    print 'afu = aml'
else :
    print 'no'

if len(x) == 2 and all_A['afu|red-pa'] == all_A['caf|ENSCAF'] == all_A['pbe|scaffo'] == all_A['mpu|ENSMPU']:
    print 'aml'
else :
    print 'no'

if len(x) == 2 and all_A['aml|ENSAME'] == all_A['caf|ENSCAF'] == all_A['pbe|scaffo'] == all_A['mpu|ENSMPU']:
    print 'afu'
else :
    print 'no'
