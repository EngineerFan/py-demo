# author  : Ryan
# datetime: 2020/10/13 20:06
# software: PyCharm

"""
description: 飞桨demo

"""

import matplotlib

matplotlib.use('Agg')
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import paddlex as pdx

from paddlex.cls import transforms

train_transforms = transforms.Compose([
    transforms.RandomCrop(crop_size=224),
    transforms.RandomHorizontalFlip(),
    transforms.Normalize()
])
eval_transforms = transforms.Compose([
    transforms.ResizeByShort(short_size=256),
    transforms.CenterCrop(crop_size=224),
    transforms.Normalize()
])

train_dataset = pdx.datasets.ImageNet(
    data_dir='vegetables_cls',
    file_list='vegetables_cls/train_list.txt',
    label_list='vegetables_cls/labels.txt',
    transforms=train_transforms,
    shuffle=True)
eval_dataset = pdx.datasets.ImageNet(
    data_dir='vegetables_cls',
    file_list='vegetables_cls/val_list.txt',
    label_list='vegetables_cls/labels.txt',
    transforms=eval_transforms)

num_classes = len(train_dataset.labels)
model = pdx.cls.MobileNetV2(num_classes=num_classes)
model.train(num_epochs=10,
            train_dataset=train_dataset,
            train_batch_size=32,
            eval_dataset=eval_dataset,
            lr_decay_epochs=[4, 6, 8],
            save_interval_epochs=1,
            learning_rate=0.025,
            save_dir='output/mobilenetv2',
            use_vdl=True)

result = model.predict('vegetables_cls/bocai/100.jpg', topk=3)
print("Predict Result:", result)
