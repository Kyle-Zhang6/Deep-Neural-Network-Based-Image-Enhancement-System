#!/usr/bin/env python
# coding: utf-8

# In[2]:


import torch
import torchvision
from torch import nn
import torch.nn.functional as F


# In[3]:


class BasicBlock(nn.Module):
    expansion = 1
    def __init__(self,channels_in,channels_out,stride=1):
        super(BasicBlock,self).__init__()
        self.conv1 = nn.Conv2d(channels_in,channels_out,kernel_size=3,padding=1,stride=stride)
        self.conv2 = nn.Conv2d(channels_out,channels_out,kernel_size=3,padding=1,stride=1)
        self.bn1 = nn.BatchNorm2d(channels_out)
        self.bn2 = nn.BatchNorm2d(channels_out)
        
        self.shortcut = nn.Sequential()
        
        if channels_in != channels_out*self.expansion or stride != 1:
            self.shortcut = nn.Sequential(
                nn.Conv2d(channels_in,channels_out*self.expansion,kernel_size=3,padding=1,stride=stride,bias=False),
                nn.BatchNorm2d(channels_out*self.expansion)
            )
        
    def forward(self,x):
        y = F.relu(self.bn1(self.conv1(x)))
        y = self.bn2(self.conv2(y))
        x = self.shortcut(x)
        return F.relu(x+y)

# BottleNeck Block
class BottleNeckBlock(nn.Module):
    expansion = 4
    def __init__(self,channels_in,channels_out,stride=1):
        super(BottleNeckBlock,self).__init__()
        self.conv1 = nn.Conv2d(channels_in,channels_out,kernel_size=1,stride=1)
        self.conv2 = nn.Conv2d(channels_out,channels_out,kernel_size=3,padding=1,stride=stride)
        self.conv3 = nn.Conv2d(channels_out,channels_out*self.expansion,kernel_size=1)
        self.bn1 = nn.BatchNorm2d(channels_out)
        self.bn2 = nn.BatchNorm2d(channels_out)
        self.bn3 = nn.BatchNorm2d(channels_out*self.expansion)
        
        self.shortcut = nn.Sequential()
        
        if channels_in != channels_out*self.expansion or stride != 1:
            self.shortcut = nn.Sequential(
                nn.Conv2d(channels_in,channels_out*self.expansion,kernel_size=3,padding=1,stride=stride,bias=False),
                nn.BatchNorm2d(channels_out*self.expansion)
            )
        
    def forward(self,x):
        y = F.relu(self.bn1(self.conv1(x)))
        y = F.relu(self.bn2(self.conv2(y)))
        y = self.bn3(self.conv3(y))
        x = self.shortcut(x)
        return F.relu(x+y)


# In[4]:


class ResNet(nn.Module):
    def __init__(self,block,layers,num_classes=1000):
        super(ResNet,self).__init__()
        self.in_planes = 64
        self.conv1 = nn.Conv2d(3,64,kernel_size=7,padding=3,stride=2)
        self.bn1 = nn.BatchNorm2d(64)
        self.maxpool = nn.MaxPool2d(kernel_size=3,padding=1,stride=2)
        
        self.layer0 = self.make_layers(block,64,layers[0])
        self.layer1 = self.make_layers(block,128,layers[1],stride=2)
        self.layer2 = self.make_layers(block,256,layers[2],stride=2)
        self.layer3 = self.make_layers(block,512,layers[3],stride=2)
        
        self.avgpool = nn.AvgPool2d(kernel_size=7,stride=1)
        self.fc = nn.Linear(512*block.expansion,num_classes)
        
        # Initiate weights of each layer
        for m in self.modules():
            if isinstance(m,nn.Conv2d):
                nn.init.kaiming_normal_(m.weight,mode='fan_out',nonlinearity='relu')
            elif isinstance(m,nn.BatchNorm2d):
                nn.init.constant_(m.weight,1)
                nn.init.constant_(m.bias,0)
        
        
    def make_layers(self,block,planes,blocks,stride=1):
        layer = []
        layer.append(block(self.in_planes,planes,stride=stride))
        self.in_planes = planes * block.expansion
        
        for i in range(blocks-1):
            layer.append(block(self.in_planes,planes))
        
        return nn.Sequential(*layer)
        
        
    def forward(self,x):
        batch_size = x.size()[0]
        x = self.conv1(x)
        x = self.bn1(x)
        x = F.relu(x)
        x = self.maxpool(x)
        
        x = self.layer0(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        
        x = self.avgpool(x)
        x = x.view(batch_size,-1)
        x = self.fc(x)
        return x

