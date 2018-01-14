path = '../images/typeStr/00_0.txt'
result_path='../images/typeStr/000.txt'
file=open(path,'r')
result_file=open(result_path,'w')
dict={}
for line in file:
    try:
        strs=line.split(':')
        encodeStr=strs[1].strip()
        if dict.has_key(encodeStr):
            dict[encodeStr]+=1
        else:
            dict[encodeStr]=1
    except:
        continue
for (k,v) in dict.items():
    result_file.write(k+':'+str(v)+'\n')
result_file.close()