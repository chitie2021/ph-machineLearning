import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-", color='black', lw=1.5)

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    plt.annotate(nodeTxt, xy=centerPt, xycoords='axes fraction', ha='center', va='center', bbox=nodeType)
    plt.annotate('', xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction',
                 arrowprops=arrow_args)

def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    
    plotNode('Decision Node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('Leaf Node', (0.8, 0.1), (0.3, 0.8), leafNode)
    
    plt.show()

def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if isinstance(secondDict[key], dict):
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if isinstance(secondDict[key], dict):
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

def retrieveTree(i):
    listOfTrees = [
        {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
        {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: {'head': {0: 'no', 1: 'yes'}}}}}},
        {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: {'head': {0: 'yes', 1: 'no'}}}}}}
    ]
    return listOfTrees[i]

def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    plt.text(xMid, yMid, txtString)

def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff -= 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff += 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff += 1.0 / plotTree.totalD

def createPlot(myTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[], frameon=False)
    createPlot.ax1 = plt.subplot(111, **axprops)
    
    plotTree.totalW = float(getNumLeafs(myTree))
    plotTree.totalD = float(getTreeDepth(myTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    
    plotTree(myTree, (0.5, 1.0), '')
    plt.show()

    return fig

if __name__ == '__main__':
    myTree = retrieveTree(0)
    createPlot(myTree)
    
    myTree = retrieveTree(1)
    createPlot(myTree)
    
    myTree = retrieveTree(2)
    createPlot(myTree)
    
    # Example usage of getNumLeafs and getTreeDepth
    print("Number of leafs:", getNumLeafs(myTree))
    print("Depth of tree:", getTreeDepth(myTree))