# author  : Ryan
# datetime: 2020/9/17 20:07
# software: PyCharm

"""
description: 文本读取工具类

"""

import jieba
from typing import List


def readTxt():
    fTxt = open('C:\\Users\\admin\\PycharmProjects\\py-demo\\data\\books\\盗墓笔记少年篇沙海.txt')
    x = fTxt.read()
    fTxt.close()
    return x


def fluAlz(wordList: List[str]) -> List[str]:
    wordSet = list(set(wordList))
    fluence = []
    for x in range(len(wordSet)):
        fluence.append([wordSet[x], wordList.count(wordSet[x])])
    fluence = sorted(fluence, key=lambda flu: flu[1], reverse=True)
    return fluence


# wordList = jieba.lcut(readTxt())
# fluence = fluAlz(wordList)
# fWrite = open('../../data/dic.txt', 'w')
# fWrite.close()
# print(wordList)


f = open('C:\\Users\\admin\\PycharmProjects\\py-demo\\data\\dict.small.txt', 'r', encoding='UTF-8')
line = f.readline()
while line:
    print(line)
    line = f.readline()
