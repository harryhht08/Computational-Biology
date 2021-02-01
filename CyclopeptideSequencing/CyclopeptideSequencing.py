def main():
    file = open('input', 'r')
    spec = ' '.join(file.readlines())
    spec = spec.strip()
    file.close()
    spec = spec.split()
    spec = list(map(int, spec))
    finalPeps = CyclopeptideSequencing(spec)
    output = formatOutput(finalPeps)
    file = open('output', 'w')
    file.write(output)
    file.close()


def CyclopeptideSequencing(Spectrum):
    candPeps = [()]
    finalPeps = []
    masses = [57,  71,  87, 97, 99,  101, 103, 113, 114, 115,
              128, 129, 131, 137, 147, 156, 163, 186]
    masses = filterSpectrum(Spectrum, masses)
    while len(candPeps) != 0:
        candPeps = expand(candPeps, masses)
        end = len(candPeps) - 1
        i = 0
        while i <= end:
            p = candPeps[i]
            listOfMass = Cyclospectrum(p)
            listOfMass_partial = Cyclospectrum_partial(p)

            if sum(p) == max(Spectrum):
                if compareTwoLists(listOfMass, Spectrum) and not checkExisted(p, finalPeps):
                    finalPeps.append(p)
                candPeps.pop(i)
                end -= 1
                i -= 1

            elif sum(p) > max(Spectrum) or not checkConsistency(listOfMass_partial, Spectrum):
                candPeps.pop(i)
                end -= 1
                i -= 1
            i += 1

    return finalPeps


def compareTwoLists(l1, l2):
    l1.sort()
    l2.sort()
    return l1 == l2


def Cyclospectrum(p):
    i = 1
    out = [0]  # mass of 0 needs to be included
    out.append(sum(p))  # mass of all elements
    while i <= len(p) - 1:
        for startIndex in range(len(p)):
            mass = 0
            for index in range(startIndex, startIndex + i):
                if index >= len(p):
                    mass += p[index - len(p)]
                else:
                    mass += p[index]
            out.append(mass)
        i += 1
    return out


# Return partial listOfMass, that is, since the candidate peptides list is not fully built yet, we can't do circulations
def Cyclospectrum_partial(p):
    i = 1
    out = [0]  # mass of 0 needs to be included
    out.append(sum(p))  # mass of all elements
    while i <= len(p) - 1:
        for startIndex in range(len(p)):
            if startIndex + i - 1 >= len(p):
                break
            mass = 0
            for index in range(startIndex, startIndex + i):
                mass += p[index]
            out.append(mass)
        i += 1
    return out


def filterSpectrum(spec, original):
    out = []
    for i in original:
        if i in spec:
            out.append(i)
    return out


# key point: use tuple datatype instead of list, since list is mutable
def expand(oldList, l1):
    newList = []
    for i in range(len(oldList)):
        for j in range(len(l1)):
            newList.append(oldList[i]+(l1[j],))
    return newList


def copyList(ol):
    nl = []
    for i in range(len(ol)):
        nl.append(ol[i])
    return nl


def checkExisted(p, peps):
    for i in peps:
        if len(i) == len(p):
            for j in range(len(p)):
                if p[j] != i[j]:
                    break
                elif j == len(p) - 1:  # the only true case would be when the last digit is equal
                    return True
    return False


def checkConsistency(l, spec):
    l.sort()
    spec.sort()
    p1 = 0
    p2 = 0
    while p1 < len(l):
        while p2 < len(spec) and spec[p2] != l[p1]:
            p2 += 1
        if p2 == len(spec):
            return False
        else:
            p1 += 1
            p2 += 1
    return True


# Convert the integer list to ideal output format
def formatOutput(peps):
    s = ""
    for i in peps:
        for j in i:
            s += str(j) + '-'
        s = s[0: len(s) - 1]
        s += ' '
    return s


main()
