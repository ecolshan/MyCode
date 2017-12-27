#!/usr/bin/env python
import os
X = {}
k = ''
count = 0
for i in os.listdir('/home/wuq/projects/convergence/workShop/'):
    X[i] = 0

for k in open('/home/wuq/projects/convergence/faa_list/faa_list.txt'):   
    
    if not X.has_key(k.strip('\n')):
       count += 1
       print k.strip('\n')#,count
