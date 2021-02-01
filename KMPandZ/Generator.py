import random
l = ['A', 'C', 'G', 'T']
s = ''
for i in range(50000000):
    a = random.randint(0, 3)
    s += l[a]
f = open('input_dna_seq', 'w')
f.write(s)
f.close()
