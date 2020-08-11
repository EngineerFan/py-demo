# author  : Ryan
# datetime: 2020/7/29 10:07
# software: PyCharm

"""
description:

"""

import torch as t

# print(t.Tensor([[1, 23, 34], [43, 66, 67]]).size())
b = t.arange(0, 6).view(2, 3)
# print(b.unsqueeze(1))