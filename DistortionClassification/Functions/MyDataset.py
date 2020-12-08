#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from torch.utils.data import DataLoader,Dataset
import os
from PIL import Image
import random

class MyDataset(Dataset):
    def __init__(self,root,transform):
        self.root = root
        self.transform = transform
        self.imgs = list(sorted(os.listdir(root)))
        #random.shuffle(self.imgs)
        self.classes = ['Motion Blur','Additive Gaussian noise','JPEG compression']
        
    def __getitem__(self,idx):
        img_path = os.path.join(self.root,self.imgs[idx])
        img = Image.open(img_path).convert('RGB')
        target = int(self.imgs[idx][6:8]) # Currently take no consideration of the degree of distortion
        if self.transform is not None:
            img = self.transform(img)
        
        return img, target
    
    def __len__(self):
        return len(self.imgs)

