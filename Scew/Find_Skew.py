file = open('input', 'r')
gene = ''.join(file.read().splitlines())
gene = gene.replace(' ', '')
gene = gene.replace('\n', '')
file.close()
scew = 0
scew_list = [0]
if len(gene) > 1:
    for x in gene:
        if x.lower() == 'C'.lower():
            scew -= 1
        elif x.lower() == 'G'.lower():
            scew += 1
        scew_list.append(scew)
mini = min(scew_list)
output = []
for i in range(0, len(scew_list)):
    if scew_list[i] == mini:
        output.append(i)
file = open('output', 'w')
for ele in output:
    file.write('%d ' % ele)
file.close()
