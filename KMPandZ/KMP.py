file = open('input', 'r')
gene = file.readlines()[1:]
file.close()
for i in range(0, len(gene)):
    gene[i] = gene[i].strip()
dna = ''.join(gene)
j = 0
i = 1
l = len(dna)
sp = [0] * l
while i < l and j < l:
    if dna[i] == dna[j]:
        sp[i] = j + 1
        i += 1
        j += 1
    elif j == 0 and dna[i] != dna[j]:
        sp[i] = 0
        i += 1
    elif dna[i] != dna[j]:
        sp[i] = 0
        j = sp[j - 1]

str = ' '.join(str(n) for n in sp)
file = open('output', 'w')
file.write(str)
file.close()
