#!/usr/bin/env python
import os
all = {}
for i in open('/home/wuq/projects/convergence/all_list.txt'):
    #print i.strip().split('\t');raw_input()
    gene_all = i.strip().split('\t')[3]
    family_all = i.strip().split('\t')[0]
    all[gene_all] = family_all
    #print all;raw_input()
fh = open('/home/wuq/projects/convergence/gene.txt','w')
fh.write('Energy:'+'\n')
a = 0
for j in open('/home/wuq/projects/convergence/allEnergyRelatedGene.tsv'):
    gene_energy = j.strip().split('\t')[1]
    #print gene_energy;raw_input()
    if all.has_key(gene_energy):
       a += 1
       #print all[gene_energy];raw_input()
       fh.write(all[gene_energy]+'\n')
fh.write('Limb:'+'\n')
b = 0
for k in open('/home/wuq/projects/convergence/allLimbRelatedGene.tsv'):
    gene_limb = k.strip().split('\t')[1]
    if all.has_key(gene_limb):
       b += 1
       fh.write(all[gene_limb]+'\n')
fh.close()
print a,b


