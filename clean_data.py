import re

def clean(filename1,filename2):
    fr = open(filename1)
    fh = open(filename2, 'w', encoding='utf-8')
    for line in fr.readlines():
        temp = str(line)
        print("原",temp)
        result = re.sub('[(&|;|\-|)]*','',temp)
        print("后",result)
        fh.write(result)
    fr.close()
    fh.close()

clean('clean.txt','clean_out.txt')
