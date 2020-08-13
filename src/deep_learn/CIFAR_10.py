# author  : Ryan
# datetime: 2020/8/13 13:48
# software: PyCharm

"""
description: CIFAR-10

"""
import torch as t
import torch.utils.data.dataloader as dataloader
import torch.utils.data.dataset as dataset
import torchvision as tv
import torchvision.transforms as transforms
from torchvision.transforms import ToPILImage

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = tv.datasets.CIFAR10(root='/home/cy/data/', train=True, download=True, transform=transform)

trainloader = dataloader.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

testset = tv.datasets.CIFAR10('/home/cy/data/', train=True, download=True, transform=transform)
testloader = dataloader.DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

show = ToPILImage()
(data, label) = trainset[100]
# print(classes[label])
print(data)
print('*' * 100)
print(((data + 1) / 2))
show(((data + 1) / 2).resize((100, 100)))
