如果你在实际做项目的过程不知道所用的质量体系（经验丰富者是可以直接看出来的），那么可以用我下面这一段代码，简单地做个检查:
less $1 | head -n 1000 | awk '{if(NR%4==0) printf("%s",$0);}' \
| od -A n -t u1 -v \
| awk 'BEGIN{min=100;max=0;} \
  {for(i=1;i<=NF;i++) {if($i>max) max=$i; if($i<min) min=$i;}}END \
  {if(max<=126 && min<59) print "Phred33"; \
  else if(max>73 && min>=64) print "Phred64"; \
  else if(min>=59 && min<64 && max>73) print "Solexa64"; \
  else print "Unknown score encoding"; \
  print "( " min ", " max, ")";}'
  
将上面这段代码复制到任意一份shell文件中（比如：fq_qual_type.sh），就可以用它来进行质量值类型的检查了。代码的思路其实比较简单，就是截取FASTQ文件的前1000行数据，并抽取出质量值所在的行，分别计算出其中最小和最大的ASCII值，再比较一下就判断出来了。下面给出一个例子，这是我们在本文中用到的FASTQ文件，它是Phred33的：
$ sh fq_qual_type.sh untreated.fq
Phred33
( 34, 67 )


我的应用实例
[wuq@localhost-3 ~/shan/reference/mydata]$ gunzip -c KPGP-00001_L1_R1.fq.gz | sh fq_qual_type.sh
Phred64
( 66, 103 )


[wuq@localhost-3 ~/shan/wgs/polarBear]$ sh fq_qual_type.sh SRR933670_1.fastq
Phred33
( 37, 67 )
  
