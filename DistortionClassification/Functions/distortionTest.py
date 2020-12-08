#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import torchvision
from torch import nn
import torch.nn.functional as F
from PIL import Image

transform = torchvision.transforms.Compose([
        torchvision.transforms.CenterCrop([200,200]),
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize([0.4955,0.4544,0.4145],[0.2975,0.2894,0.3006])
        # torchvision.transforms.Normalize([0.4955,0.4544,0.4145],[0.2975,0.2894,0.3006])
    ])

transform5 = torchvision.transforms.Compose([
        torchvision.transforms.FiveCrop([200,200]),
        torchvision.transforms.ToTensor(),
        #torchvision.transforms.Lambda(lambda crops: torch.stack([torchvision.transforms.ToTensor()(crop) for crop in crops])),
        torchvision.transforms.Lambda(lambda crops: torch.stack(
            [torchvision.transforms.Normalize([0.4955,0.4544,0.4145],[0.2975,0.2894,0.3006])(crop) for crop in crops]
         ))
        #torchvision.transforms.Normalize([0.4955,0.4544,0.4145],[0.2975,0.2894,0.3006])
    ])

transform10 = torchvision.transforms.Compose([
        torchvision.transforms.TenCrop([200,200]),
        torchvision.transforms.Lambda(lambda crops: torch.stack([torchvision.transforms.ToTensor()(crop) for crop in crops])),
        torchvision.transforms.Lambda(lambda crops: torch.stack(
            [torchvision.transforms.Normalize([0.4955,0.4544,0.4145],[0.2975,0.2894,0.3006])(crop) for crop in crops]
        ))
        # torchvision.transforms.Normalize([0.4955,0.4544,0.4145],[0.2975,0.2894,0.3006])
    ])
# In[ ]:


def distortionTest(net,device,img_path,crop=5):

    if crop == 1:
        imgs = transform(Image.open(img_path))
        imgs = imgs.view(1,3,200,200)
    elif crop == 5:
        imgs = transform5(Image.open(img_path))
    elif crop == 10:
        imgs = transform10(Image.open(img_path))
    imgs = imgs.to(device)
    net.to(device)
    
    net.eval()
    with torch.no_grad():
        result = net(imgs)
        _,predicted = torch.max(result,dim=1)
        
    return predicted

def getRawResult(net,device,img_path,crop=5):
    if crop == 1:
        imgs = transform(Image.open(img_path))
        imgs = imgs.view(1, 3, 200, 200)
    elif crop == 5:
        imgs = transform5(Image.open(img_path))
    elif crop == 10:
        imgs = transform10(Image.open(img_path))
    imgs = imgs.to(device)
    net.to(device)

    net.eval()
    with torch.no_grad():
        result = net(imgs)

    return result

