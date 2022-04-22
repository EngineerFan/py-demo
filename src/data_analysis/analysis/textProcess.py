# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/10/20 21:58
# @Software    : PyCharm
# @Description :


import pandas as pd
import jieba

df = pd.read_csv('../../data/神医柳下惠_黑道书(HEIDAOSHU.COM).txt', encoding='utf-8', header=None, sep='\t')
string = df.iloc[4, 0]
seg_list = jieba.cut(string, cut_all=False)
print('/'.join(list(seg_list)))
