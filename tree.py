#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
决策树的算法原理：
1.获取原始的数据集，基于最好的特征划分数据集（由于特征值可能多于2个，则可能存在大于2个分支的数据集划分）
2.第一次划分之后，数据将被向下传递给树的分支的下一个节点，在这个节点上，利用递归的原理再次划分数据集
递归结束的条件：
1.分支下的所有实例都具有相同的分类（任何到达该叶子节点的数据，必然属于该叶子节点的分类）
2.程序遍历完划分数据集的所有特征（此时如果该叶子节点的类标签不唯一，则取出现次数最多的类别标签）
"""

import pdb
import numpy as np
import operator

from math import log


class tree(object):
    def __init__(self):
        self.dataSet = [] # 训练样本
        self.labels = []  # 特征标签

    # 训练样本
    def creatDateSet(self):
        self.dataSet = [[1, 1, "yes"],
                        [1, 1, "yes"],
                        [1, 0, "no"],
                        [0, 1, "no"],
                        [0, 1, "no"]]  # 1代表是，0代表否。前两列代表特征，最后一列代表训练样本数据的类别
        self.labels = ["no surfacing", "flippers"]  # 特征标签
        # print self.dateSet
        # print self.labels

    # 计算数据集的香农熵
    def calcShannonEnt(self, data):
        numEntries = len(data)  # 数据集的数量
        labelCounts = {}
        for featVec in data:
            currentLabel = featVec[-1]  # 取数据集分类的类别
            labelCounts[currentLabel] = labelCounts.get(currentLabel, 0) + 1  # 统计数据集的不同类别的频数

        shannonEnt = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key])/numEntries  # 计算数据集的不同类别对应的概率
            shannonEnt = -(prob*log(prob, 2)) + shannonEnt  # 计算数据集的类别的香农熵
        return shannonEnt

    # 选取特征值划分数据集
    def splitDataSet(self, data, axis, value):
        retDataSet = []
        for featVec in data:
            if int(featVec[axis]) == value:   # 输入特征的位置axis，输入特征值value
                reducedFeatVec = featVec[: axis]
                reducedFeatVec.extend(featVec[axis+1:])
                retDataSet.append(reducedFeatVec)  # 该特征值对应的数据集的子集
        return retDataSet

    # 选取最好的特征划分数据集
    def chooseBestFeatureToSplit(self, data):
        numFeatures = len(data[0]) - 1  # 特征的数量
        baseEntropy = self.calcShannonEnt(data)  # 计算数据集的原始香农熵
        bestInfoGain = 0.0  # 初始化最大的信息增益
        bestFeature = -1  # 初始化最好的特征
        for i in range(numFeatures):
            featList = [example[i] for example in data]  # 提取特征值
            uniqueVals = set(featList)  # 去除重复的特征值
            newEntropy = 0.0  # 初始化条件熵
            for value in uniqueVals:
                subDateSet = self.splitDataSet(data, i, value)  # 按照特征值划分数据集
                prob = len(subDateSet)/float(len(data))  # 计算该特征值的概率
                newEntropy = newEntropy + prob*self.calcShannonEnt(subDateSet)  # 计算特征对应的条件熵
            # print newEntropy
            infoGain = baseEntropy - newEntropy  # 计算特征对应的信息增益
            if infoGain > bestInfoGain:
                bestInfoGain = infoGain  # 取最大的信息增益
                bestFeature = i  # 最大的信息增益对应的特征
        return bestFeature

    # 当训练样本已经处理了所有的属性，但是部分叶子节点的类标签仍然不是唯一的，将出现次数最多的类标签作为该叶子节点的标签
    def majorityCnt(self, classList):
        classCount = {}
        for vote in classList:
            classCount[vote] = classCount.get(vote, 0) + 1  # 统计不同标签的频数
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)  # 对标签的频数进行降序排序
        return sortedClassCount[0][0]  # 返回出现次数最多的标签

    # 构建决策树
    def createTree(self, data, label):
        classList = [example[-1] for example in data]  # 提取训练样本的分类标签
        if classList.count(classList[0]) == len(classList):  # 如果分支下的标签只有一种
            return classList[0]  # 返回该叶子节点的类别
        if len(data[0]) == 1:  # 当数据集已经处理了所有的属性，且类别标签不唯一
            return self.majorityCnt(classList)  # 将出现次数最多的类标签作为该叶子节点的标签
        bestFeat = self.chooseBestFeatureToSplit(data)  # 选择最好的特征划分数据集
        bestFeatLabel = label[bestFeat]  # 最好的特征标签名
        myTree = {bestFeatLabel: {}}  # 决策树
        clabels = label[:]  # 保证不改动原始的标签列表
        del(clabels[bestFeat])  # 从特征标签列表中删除该标签
        featValues = [example[bestFeat] for example in data]  # 读取该特征的值
        uniqueVals = set(featValues)  # 去除重复的特征值
        for value in uniqueVals:
            subLabels = clabels[:]  # 保证每次调用createTree()时，不改变原始列表的内容
            myTree[bestFeatLabel][value] = self.createTree(self.splitDataSet(data, bestFeat, value), subLabels)  # 递归构建决策树

        return myTree



if __name__ == "__main__":
    tit = tree()
    tit.creatDateSet()
    #result = tit.calcShannonEnt(tit.dataSet)
    #ret = tit.splitDataSet(1, 1)
    #bFeature = tit.chooseBestFeatureToSplit(tit.dataSet)
    tree = tit.createTree(tit.dataSet, tit.labels)
    #print ret
    #print result
    #print bFeature
    print tree, tit.labels


    print "----done-----"

"""
训练样本的类别     训练样本的数量      香农熵
      2                 5             0.970950594455
      3                 6             1.45914791703
      2                 6             0.918295834054
      3                 5             1.37095059445
给数据集添加更多的类别，混合数据越多，熵越高，包含的信息量越大
"""