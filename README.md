# Calculate-contig-N50

基因组的统计信息包含GC含量，N50等等，这里我们计算N50的算法:
N50是指一个基因组所有的contig，按照长度从大到小排列，一直长度加和，一直到某条contig达到该
基因组总共长度的1/2时，那么这条contig的长度，就是N50的值。N50可以作为评价一个基因组拼接
好坏的条件之一。
