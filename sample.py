f = open('../bioinfo_input/fastq_files/PE_1.fastq','r+')
data = f.readlines()
for i in data[1:10]:
    print(i)
