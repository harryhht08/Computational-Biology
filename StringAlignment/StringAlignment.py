
def main():
    file = open('input', 'r')
    s1, s2 = file.readlines()
    s1 = s1.strip()
    s2 = s2.strip()
    file.close()
    BLOSUM62, mapLetterToIndex = initBLOSUM62()
    mat = initMatrix(s1, s2)
    score, sout1, sout2 = alignStrings(mat, s1, s2, BLOSUM62, mapLetterToIndex)
    file = open('output', 'w')
    file.write(str(score) + '\n' + str(sout1) + '\n' + str(sout2))


def initMatrix(s1, s2):
    rows = len(s2) + 1
    matrix = []
    for i in range(rows):
        matrix.append([])
    return matrix


def initBLOSUM62():
    BLOSUM62 = []
    mapLetterToIndex = {}
    file = open('BLOSUM62.txt', 'r')
    lines = file.readlines()
    file.close()
    letterList = lines[0].split()
    for i in range(len(letterList)):
        mapLetterToIndex[letterList[i]] = i
    for line in lines[1:]:
        BLOSUM62.append([int(x) for x in line.split()[1:]])
    return BLOSUM62, mapLetterToIndex


def alignStrings(mat, s1, s2, blosum, mapping):
    sigma = 5
    for i in range(len(s1) + 1):
        if i == 0:
            mat[0].append(0)
        else:
            mat[0].append(mat[0][i - 1] - sigma)
    for j in range(1, len(mat)):
        mat[j].append(mat[j - 1][0] - sigma)

    for i in range(1, len(mat)):
        for j in range(1, len(s1) + 1):
            compValue = blosum[mapping[s1[j - 1]]][mapping[s2[i - 1]]]
            mat[i].append(max(mat[i-1][j-1]+compValue,
                              mat[i-1][j]-sigma, mat[i][j-1]-sigma))

    # Get the last number in the last row of the matrix
    score = mat[-1][-1]

    sout1 = ''
    sout2 = ''
    sout1, sout2 = wayBackHome(len(mat) - 1, len(mat[i]) - 1,
                               mat, sout1, sout2, blosum, mapping, sigma, s1, s2)
    sout1 = sout1[::-1]
    sout2 = sout2[::-1]

    return score, sout1, sout2


# The Korean song named Way Back Home is good! Just saying.
def wayBackHome(i, j, mat, sout1, sout2, blosum, mapping, sigma, s1, s2):
    if i == 0 and j == 0:
        return sout1, sout2

    if mat[i][j] == mat[i-1][j] - sigma:
        return wayBackHome(i-1, j, mat, sout1 + '-', sout2 + s2[i-1], blosum, mapping, sigma, s1, s2)
    if mat[i][j] == mat[i][j-1] - sigma:
        return wayBackHome(i, j-1, mat, sout1 + s1[j-1], sout2 + '-', blosum, mapping, sigma, s1, s2)
    else:
        return wayBackHome(i-1, j-1, mat, sout1 + s1[j-1], sout2 + s2[i-1], blosum, mapping, sigma, s1, s2)


main()
