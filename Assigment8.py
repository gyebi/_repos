file_name = input('please enter file name :')
fh = open(file_name)


counts = dict()
for line in fh: 
    words = line.split()
    for word in words : 
        counts[word] = counts.get(word, 0) +1

#print('Words:', words)
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount: 
        bigcount = word 
        bigcount = count 
print(bigword, bigcount)

print('Counts', counts) 