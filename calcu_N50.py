#以sequence.fasta 为列，来计算50的值
#基因组拼接时，contig是按照长度从大到小排列的
f = open('sequence.fasta','r').readlines()
total_length =0
for i in f:
  if not i.startswith('>'):
    seq_length = len(i.strip())
    total_length += seq_length

variable_length =0
for i in f:
  if not i.startswith('>'):
    seq_length = len(i.strip())
    variable_length += seq_length
    if variable_length >= total_length /2:
      print('N50 :%s'%seq_length)  #输出N50的值
      break
