gene = 'GAAATAAA'
min_length_string = len(gene)
     
occurences = dict()
occurences['A'] = 0
occurences['G'] = 0
occurences['C'] = 0
occurences['T'] = 0
 
expected = len(gene) // 4
 
for g in gene:
    occurences[g] += 1
 
for x in occurences:
    occurences[x] = max(0, occurences[x] - expected)
 
if occurences['A'] == 0 and occurences['G'] == 0 and occurences['C'] == 0 and occurences['T'] == 0:
    print(0) 
 
found = dict()
found['A'] = 0
found['G'] = 0
found['C'] = 0
found['T'] = 0
     
tail = 0
head = 0
     
while head != len(gene):
    found[gene[head]] += 1
    if found['A'] >= occurences['A'] and \
    found['C'] >= occurences['C'] and \
    found['G'] >= occurences['G'] and \
    found['T'] >= occurences['T']:
        # this is a valid candidate
        min_length_string = min(min_length_string, head-tail+1)
             
            # try to shorten it
        while found[gene[tail]] > occurences[gene[tail]]:
            found[gene[tail]] -= 1
            tail += 1
            min_length_string = min(min_length_string, head-tail+1)
             
             
    head += 1
     
print(min_length_string)
