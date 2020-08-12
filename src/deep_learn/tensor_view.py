# author  : Ryan
# datetime: 2020/8/12 8:56
# software: PyCharm

"""
description:  tensor view

"""

import torch as t
import numpy as np
from torch.autograd import Variable

import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(x.size()[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()
input = Variable(t.randn(1, 1, 32, 32))
print(input)
output = net(input)
print('*' * 100)
print(output)
target = Variable(t.arange(0, 10).reshape((1, 10)))
print(target)
criterion = nn.MSELoss()
loss = criterion(output, target)
print(loss)
print('*' * 100)
net.zero_grad()
print('反向传播之前conv1.bias的梯度')
print(net.conv1.bias)
loss.backward()
print('反向传播之后conv1.bias的梯度')
print(net.conv1.bias.grad)
