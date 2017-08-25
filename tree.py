#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

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
    def chooseBestFeatureToSplit(self):
        numFeatures = len(self.dataSet[0]) - 1  # 特征的数量
        baseEntropy = self.calcShannonEnt(self.dataSet)  # 计算训练数据集的原始香农熵
        bestInfoGain = 0.0  # 初始化最大的信息增益
        bestFeature = -1  # 初始化最好的特征
        for i in range(numFeatures):
            featList = [example[i] for example in self.dataSet]  # 提取特征值
            uniqueVals = set(featList)  # 去除重复的特征值
            newEntropy = 0.0  # 初始化条件熵
            for value in uniqueVals:
                subDateSet = self.splitDataSet(self.dataSet, i, value)  # 按照特征值划分数据集
                prob = len(subDateSet)/float(len(self.dataSet))  # 计算该特征值的概率
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
            if vote not in classCount.keys():
                classCount[vote] = 0
            classCount[vote] = classCount[vote] + 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    def createTree(self):



if __name__ == "__main__":
    tit = tree()
    tit.creatDateSet()
    result = tit.calcShannonEnt(tit.dataSet)
    #ret = tit.splitDataSet(1, 1)
    bFeature = tit.chooseBestFeatureToSplit()
    #print ret
    #print result
    print bFeature


    print "----done-----"

"""
训练样本的类别     训练样本的数量      香农熵
      2                 5             0.970950594455
      3                 6             1.45914791703
      2                 6             0.918295834054
      3                 5             1.37095059445
给数据集添加更多的类别，混合数据越多，熵越高，包含的信息量越大
"""