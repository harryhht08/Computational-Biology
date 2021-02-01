def main():
    file = open('input', 'r')
    n = int(file.readline().strip())
    matrix = []
    unchangedMatrix = []
    for line in file.readlines():
        matrix.append(list(float(x) for x in line.strip().split()))
        unchangedMatrix.append(list(float(x) for x in line.strip().split()))
    file.close()
    listOfData = list([x] for x in range(n))
    output = []
    while len(matrix) > 1:
        output.append(merge(matrix, listOfData, unchangedMatrix))
    outputString = ""
    for a in output:
        for b in a:
            outputString += str(b + 1) + ' '
        outputString += '\n'
    file = open('output', 'w')
    file.write(outputString)


def updateMatrix(matrix, newRowIndex, biggerIndex, listOfData, originalMatrix):
    newRow = []
    newRowData = listOfData[newRowIndex] + listOfData[biggerIndex]
    for i in range(len(listOfData)):
        if i != newRowIndex and i != biggerIndex:
            currData = listOfData[i]
            sum = 0
            for a in currData:
                for b in newRowData:
                    sum += originalMatrix[a][b]
            newRow.append(sum / (len(newRowData * len(currData))))

    cursor = 0
    for i in range(len(matrix)):
        if i != newRowIndex and i != biggerIndex:
            matrix[i].pop(biggerIndex)
            matrix[i][newRowIndex] = newRow[cursor]
            cursor += 1
    newRow.insert(newRowIndex, 0.0)

    matrix.pop(biggerIndex)
    matrix.pop(newRowIndex)
    matrix.insert(newRowIndex, newRow)

    out = tuple(listOfData[newRowIndex] + listOfData[biggerIndex])
    listOfData.pop(biggerIndex)
    listOfData.pop(newRowIndex)
    listOfData.insert(newRowIndex, list(out))
    return out


def merge(matrix, listOfData, originalMatrix):
    min = matrix[0][1]
    for r in matrix:
        for c in r:
            if c != 0 and c < min:
                min = c

    minIndex = (-1, -1)
    for rowIndex in range(len(matrix)):
        row = matrix[rowIndex]
        for index in range(len(row)):
            if row[index] == min:
                minIndex = (rowIndex, index)

    if minIndex[0] > minIndex[1]:
        newRowIndex = minIndex[1]
        biggerIndex = minIndex[0]
    else:
        newRowIndex = minIndex[0]
        biggerIndex = minIndex[1]

    return updateMatrix(matrix, newRowIndex, biggerIndex, listOfData, originalMatrix)


main()
