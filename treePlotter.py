#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
绘制决策树
"""

import pdb

import matplotlib.pyplot as plt


class treePlot(object):
    def __init__(self):
        self.decisionNode = dict(boxstyle="sawtooth", fc="0.8")  # 定义决策节点的文本框类型和颜色深度
        self.leafNode = dict(boxstyle="round4", fc="0.8")  # 定义叶子节点的文本框类型和颜色深度
        self.arrow_args = dict(arrowstyle="<-")  # 定义箭头的格式

    # 绘图的函数
    def plotNode(self, createPlot_ax1, nodeTxt, centerPt, parentPt, nodeType):
        createPlot_ax1.annotate(nodeTxt, xy=parentPt, xycoords="axes fraction", xytext=centerPt,
                                textcoords="axes fraction", va="center", ha="center", bbox=nodeType,
                                arrowprops=self.arrow_args)
        # nodeTxt为文本框内的内容，即标注文本。xy为所要标注的位置坐标，xytext为标注文本所在的位置，arrowprops为标注的箭头格式，bbox为文本框的类型

    # 调用plotNode函数绘图
    def createPlot_bak(self):
        fig = plt.figure(1, facecolor="white")  # 创建一幅图，图片的背景为白色
        fig.clf()  # 清空绘图区
        createPlot_ax1 = plt.subplot(111, frameon=False)  # 图分隔为1行1列，图像画在从左到右从上到下的第1块
        self.plotNode(createPlot_ax1, "a decision node", (0.5, 0.1), (0.1, 0.5), self.decisionNode)  # 绘制决策节点的图
        self.plotNode(createPlot_ax1, "a leaf node", (0.8, 0.1), (0.3, 0.8), self.leafNode)  # 绘制叶子节点的图
        plt.show()

    # 存储决策树的信息
    def retrieveTree(self, i):
        listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                       {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]  # 存储的两颗决策树的信息
        return listOfTrees[i]

    # 统计决策树的叶子节点的数目
    def getNumLeafs(self, myTree):
        numLeafs = 0
        firstStr = myTree.keys()[0]  # 树的第一个节点
        secondDict = myTree[firstStr]  # 树的第一个节点对应的键值
        for key in secondDict.keys():
            if type(secondDict[key]).__name__ == "dict":  # 节点的键值为字典格式
                numLeafs = numLeafs + self.getNumLeafs(secondDict[key])  # 则递归调用计算该字典内的叶子节点
            else:
                numLeafs = numLeafs + 1  # 节点的键值不是字典格式，则累加1

        return numLeafs

    # 统计决策树的层数
    def getTreeDepth(self, myTree):
        maxDepth = 0
        firstStr = myTree.keys()[0]
        secondDict = myTree[firstStr]
        for key in secondDict.keys():
            if type(secondDict[key]).__name__ == "dict":
                thisDepth = 1 + self.getTreeDepth(secondDict[key])  # 节点键值为字典格式，则递归调用计算字典的层数
            else:
                thisDepth = 1  # 节点的键值非字典格式，则层数计为1

            if thisDepth > maxDepth:
                maxDepth = thisDepth  # 返回最大的层数

        return maxDepth

    def plotMidText(self, createPlot_ax2, cntrPt, parentPt, txtString):
        xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
        yMid = (parentPt[1] - cntrPt[1])/2.0 + cntrPt[1]
        createPlot_ax2.text(xMid, yMid, txtString)

    def plotTree(self, createPlot_ax2, plotree_totalW, plotree_totalD, plotree_xOff, plotree_yOff, myTree, parentPt, nodeTxt):
        numLeafs = self.getNumLeafs(myTree)
        depth = self.getTreeDepth(myTree)

        firstStr = myTree.keys()[0]
        cntrPt = (plotree_xOff + (1.0 + float(numLeafs))/2.0/plotree_totalW, plotree_yOff)
        self.plotMidText(createPlot_ax2, cntrPt, parentPt, nodeTxt)
        self.plotNode(createPlot_ax2, firstStr, cntrPt, parentPt, self.decisionNode)
        secondDict = myTree[firstStr]
        plotree_yOff = plotree_yOff - 1.0/plotree_totalD
        for key in secondDict.keys():
            if type(secondDict[key]).__name__ == "dict":
                self.plotTree(createPlot_ax2, plotree_totalW, plotree_totalD, plotree_xOff, plotree_yOff, secondDict[key], cntrPt, str(key))
            else:
                plotree_xOff = plotree_xOff + 1.0/plotree_totalW
                self.plotNode(createPlot_ax2, secondDict[key], (plotree_xOff, plotree_yOff), cntrPt, self.leafNode)
                self.plotMidText(createPlot_ax2, (plotree_xOff, plotree_yOff), cntrPt, str(key))

        plotree_yOff = plotree_yOff + 1.0/plotree_totalD

    # 绘制决策树
    def createPlot(self, myTree):
        fig = plt.figure(1, facecolor="white")
        fig.clf()
        axprops = dict(xticks=[], yticks=[])
        createPlot_ax2 = plt.subplot(111, frameon=False, **axprops)
        plotree_totalW = float(self.getNumLeafs(myTree))  # 决策树的宽度
        plotree_totalD = float(self.getTreeDepth(myTree))  # 决策树的深度
        plotree_xOff = -0.5/plotree_totalW  #
        plotree_yOff = 1.0
        self.plotTree(createPlot_ax2, plotree_totalW, plotree_totalD, plotree_xOff, plotree_yOff, myTree, (0.5, 1.0), "")
        plt.show()








if __name__ == "__main__":
    tit = treePlot()
    #tit.createPlot_bak()
    myTree = tit.retrieveTree(1)
    #NumLeafs = tit.getNumLeafs(myTree)
    #TreeDepth = tit.getTreeDepth(myTree)
    tit.createPlot(myTree)
    #print myTree
    #print NumLeafs
    #print TreeDepth
    print "----done------"
