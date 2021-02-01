def main():
    file = open('input', 'r')
    data = []
    for line in file.readlines():
        data.append(line.strip())
    file.close()
    k, dims = data[0].split()
    k = int(k)
    dims = int(dims)
    data = data[1:]
    for i in range(len(data)):
        data[i] = list(float(x) for x in data[i].split())

    currCentroids = data[:k]
    prevCentroids = []
    while not checkTwoListIdentical(currCentroids, prevCentroids):
        prevCentroids = currCentroids
        currCentroids = updateCentroids(currCentroids, data)

    output = ""
    for c in currCentroids:
        output += " ".join(str(x) for x in c) + '\n'
    file = open('output', 'w')
    file.write(output)


def checkTwoListIdentical(l1, l2):
    l1.sort()
    l2.sort()
    return l1 == l2


def updateCentroids(centroids, data):
    newCentroids = []
    clusters = []
    for i in range(len(centroids)):
        clusters.append([])
    for point in data:
        min = computeDistance(point, centroids[0])
        belongTo = 0  # the index of the centroid the current point is closest to
        for i in range(len(centroids)):
            dis = computeDistance(point, centroids[i])
            if dis < min:
                belongTo = i
                min = dis
        clusters[belongTo].append(point)
    for c in clusters:
        newCentroids.append(computeMean(c))
    return newCentroids


def computeMean(points):
    res = [sum(x) / len(x) for x in zip(*points)]
    return res


def computeDistance(a, b):
    dis = 0
    for i in range(len(a)):
        dis += (a[i] - b[i]) ** 2
    return dis ** .5


main()
