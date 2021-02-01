
def main():
    file = open('input', 'r')
    end = file.readline().strip()
    file.close()

    end = list(end)
    start = list(end)
    start.sort()    # The start list starts with $
    output = []
    output.append(end[0])
    output.append('$')

    i = end[0]
    position = 0
    while True:
        order = 1 + countNumber(i, end[:position])
        index = getIndex(order, i, start)
        i = end[index]
        if i == '$':
            break
        position = index
        output.insert(0, i)

    file = open('output', 'w')
    file.write(''.join(output))


def countNumber(c, arr):
    if arr == None or len(arr) == 0:
        return 0
    count = 0
    for i in arr:
        if c == i:
            count += 1
    return count


def getIndex(order, c, arr):
    for i in range(len(arr)):
        if arr[i] == c and order == 1:
            return i
        elif arr[i] == c:
            order -= 1


main()
