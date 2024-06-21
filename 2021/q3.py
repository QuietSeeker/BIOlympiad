
def add(seq):
    nextBox = chr(max(map(ord, seq)) + 1)
    return seq + nextBox


def swap(seq):
    if len(seq) == 1:
        return seq
    return seq[1] + seq[0] + seq[2:]


def rotate(seq):
    if len(seq) == 1:
        return seq
    return seq[1:] + seq[0]


class treeNode:
    def __init__(self, seq):
        self.seq = seq
        self.opt1 = None
        self.opt2 = None
        self.opt3 = None


class tree:

    def __init__(self, target):
        self.root = treeNode("A")
        self.states = {"A"}
        nodesAdded = [self.root]
        steps = 1

        while target not in self.states:
            node = nodesAdded[0]
            opt1 = add(node.seq)
            if opt1 not in self.states:
                node.opt1 = treeNode(opt1)
                self.states.add(opt1)
                nodesAdded.append(node.opt1)

            opt2 = swap(node.seq)
            if opt2 not in self.states:
                node.opt2 = treeNode(opt2)
                self.states.add(opt2)
                nodesAdded.append(node.opt2)

            opt3 = rotate(node.seq)
            if opt3 not in self.states:
                node.opt3 = treeNode(opt3)
                self.states.add(opt3)
                nodesAdded.append(node.opt3)

            nodesAdded.pop(0)

        self.findSteps(target)

    def findSteps(self, target):
        currLayer = [self.root]
        nextLayer = []
        found = self.root.seq == target
        steps = 1
        if found:
            print(steps)

        while not found:
            for node in currLayer:
                if node.seq == target:
                    found = True
                    print(steps)
                    break
                if node.opt1:
                    nextLayer.append(node.opt1)
                if node.opt2:
                    nextLayer.append(node.opt2)
                if node.opt3:
                    nextLayer.append(node.opt3)

            currLayer = nextLayer
            nextLayer = []
            steps += 1


b = input().upper()
tree(b)
