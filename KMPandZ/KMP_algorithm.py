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
print(sp)

# Now we've built the sp values array, start implementing the
# actual KMP algorithm.

file = open('input_dna_seq', 'r')
gene = file.readlines()
file.close()
for i in range(0, len(gene)):
    gene[i] = gene[i].strip()
gene = ''.join(gene)

p1 = 0
p2 = 0
pattern = dna
output = []
while p1 < len(gene):
    if gene[p1] == pattern[p2] and p2 == len(pattern) - 1:
        output.append(p1 - len(pattern))
        p2 = 0
    elif gene[p1] == pattern[p2]:
        p2 += 1
    else:
        if not p2 == 0:
            p2 = sp[p2 - 1]
            p1 -= 1
    p1 += 1
