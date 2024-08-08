#以sequence.fasta 为列，来计算N50的值
f= open('sequence.fasta','r').readlines()
total_length =0
total_seg =''
for i in f:
  if not i.startswith('>'):
    seq_length = len(i.strip())
    total_length += seq_length
    total_seg += i.strip()

GC_number=0
for j in total seg:
  if j == 'C' or j == 'G':
    GC_number += 1
    

GC_percent =Gc number/total length # 输出为GC含量
print(f'GC percent :{GC percent}')
