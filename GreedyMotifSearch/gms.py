def scoreMotif(k, arr):
    vertical = []
    score = 0
    for i in range(k):
        lst = []
        for j in range(len(arr)):
            lst.append(arr[j][i])
        vertical.append(lst)

    mostCommons = []
    for i in range(len(vertical)):
        mostCommons.append(max(set(vertical[i]), key=vertical[i].count))

    for i in range(len(vertical)):
        for j in vertical[i]:
            if j != mostCommons[i]:
                score += 1

    return score


def profile(k, arr):
    prof = []   # Profile is a list of dictionary, total length of k
    vertical = []
    for i in range(k):
        prof.append(dict({'a': 1, 'c': 1, 'g': 1, 't': 1}))
        lst = []
        for j in range(len(arr)):
            lst.append(arr[j][i])
        vertical.append(lst)
    for i in range(len(vertical)):
        for j in vertical[i]:
            prof[i][j.lower()] += 1
    for i in range(len(prof)):
        for j in ['a', 'c', 'g', 't']:
            prof[i][j] /= len(arr)

    return prof


def findMostProbable(k, profile, gene):
    out = gene[0:k]
    i = 0
    maxPoss = 0
    maxPossIndex = 0
    while(i + k - 1 <= len(gene) - 1):
        s = gene[i:i + k]
        possibility = 1
        for j in range(k):
            index = s[j].lower()
            possibility *= profile[j][index]
        if possibility > maxPoss:
            maxPoss = possibility
            out = s
            maxPossIndex = i
        i += 1
    return out, maxPossIndex


# arr = ['CAG', 'CAG', 'CAA', 'CAA', 'CAA']
# p = (profile(3, arr))
# print(findMostProbable(3, p, 'ACGTC'))


file = open('input', 'r')
lines = file.readlines()
k, t = lines[0].split()
k = int(k)
t = int(t)
dna = lines[1:]
file.close()

for i in range(0, len(dna)):
    dna[i] = dna[i].strip()

bestMotifs = []
for s in dna:
    bestMotifs.append(s[0:k])
for i in range(len(dna[0]) - k + 1):
    motifs = []
    m1 = dna[0][i:i + k]
    motifs.append(m1)
    if (t > 1):
        for j in range(1, t):
            prof = profile(k, motifs)
            mj, x = findMostProbable(k, prof, dna[j])
            motifs.append(mj)
    if scoreMotif(k, motifs) < scoreMotif(k, bestMotifs):
        bestMotifs = motifs

output = '\n'.join(n for n in bestMotifs)
file = open('output', 'w')
file.write(output)
file.close()

# s = profile(3, [['a', 'c', 'g'], ['c', 'c', 'g'], ['a', 'c', 'g'], ['a', 'c', 'g'], ['a', 'c', 'g'], ['a', 'c', 'g'], ['a', 'c', 'g'], [
#     'a', 'c', 'g'], ['a', 'c', 'g'], ['a', 'c', 'g'], ['a', 'c', 'g'], ['a', 'c', 'g'], ['a', 'c', 'g']])
# print(s)
