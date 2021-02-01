class Node:
    def __init__(self):
        # The children of a node is a dictionary, value: children node, key: string on edge to the children node
        self.children = {}
        self.parent = None


def createSuffixList(s):
    sList = []
    for i in range(len(s)):
        newS = s[i:]
        sList.append(newS)
    return sList


def buildTree(n, s):
    curr = n
    foundSameStart = False
    if not not curr.children:   # 'not a' is true when dict a is empty
        for k, v in curr.children.items():
            if k[0] == s[0]:
                foundSameStart = True
                for i in range(len(s)):
                    if k[i] == s[i] and i+1 == len(k):
                        if i+1 < len(s):
                            buildTree(v, s[i+1:])
                        break
                    elif k[i] != s[i]:
                        compared = s[:i]
                        uncomparedS = s[i:]
                        uncomparedK = k[i:]
                        newNode = Node()
                        newNode.parent = v.parent
                        v.parent = newNode
                        newNode.parent.children.pop(k)
                        newNode.parent.children[compared] = newNode
                        newNode.children[uncomparedK] = v
                        leaf = Node()
                        newNode.children[uncomparedS] = leaf
                        leaf.parent = newNode
                        break
    if (not foundSameStart):
        newLeaf = Node()
        newLeaf.parent = curr
        curr.children[s] = newLeaf


def getAllEdges(n, l):
    if n == None:
        return l
    for k in n.children.keys():
        l.append(k)
    for v in n.children.values():
        getAllEdges(v, l)


def main():
    file = open('input', 'r')
    lines = file.readlines()
    file.close()
    dna = ''.join(x.strip() for x in lines)
    listOfSub = createSuffixList(dna)
    root = Node()
    for s in listOfSub:
        buildTree(root, s)
    edges = []
    getAllEdges(root, edges)
    output = '\n'.join(edges)
    file = open('output', 'w')
    file.write(output)
    file.close()


main()
