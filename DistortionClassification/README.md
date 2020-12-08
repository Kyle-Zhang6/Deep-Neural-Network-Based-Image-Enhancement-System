## 分类器模型训练与测试

基于pytorch与jupyter notebook完成训练与测试；基于MATLAB完成数据集生成。



- __'TrainingModels 2.0.ipynb'__

  使用torchvision导入训练集并构建ResNet18进行分类器训练；

  训练过程中截取每张图片中间的200\*200像素作为输入；

  采用k折交叉验证（k=6），因此一共完成6个模型的训练，以参数形式存储于目录’./Models‘下；

  

- __'test 2.0.ipynb'__

  导入测试集和以完成训练的模型进行测试；

  对于一张原测试图片，可以像训练时一样截取中间200\*200像素输入；也可以使用torchvision.transform.FiveCrop()或torchvision.transform.TenCrop()截取图片中多个位置的200\*200子图片，分别使用模型进行分类，最终将统计次数最多的分类结果作为最终分类结果；

  该文件对6个模型和上述3中输入方式分别进行了测试，统计了正确率以及分类错误的图片信息，测试结果通过pandas保存于'./nets_test_info.xlsx'；

  

- __'./Functions'__

  目录下有两个类和一个方法：'MyResnet.py', 'MyDataset.py', 'distortionTest.py';

  - 'MyResnet.py'：定义了ResNet的架构，只需指定'BasicBlock'或'BottleNeck'以及四个block分别的深度即可构造各种ResNet；

    如：net = ResNet(BasicBlock, [2,2,2,2], num_classes=3)，即构造了一个三分类的ResNet18；

  - 'MyDataset.py'：定义了数据集导入与初始化的类，指定数据集路径和变换即可；

    如：dataset = MyDataset('./root',transform)；

  - 'distortionTest.py'：定义了测试用的方法，单图片输入，支持前述三种测试方式；

    

- __'./Models'__

  分别保存了训练所得的6个分类模型；

  

- __'./TrainingProcess'__

  保存了每个训练过程中的训练集损失值train_loss，验证集损失值val_loss，以及验证集正确率；

  

- __'./data'__

  数据集目录；

  目录下的'kFolderSplit.m'使用MATLAB将训练集随机等分成k个子训练集，用来为k折交叉验证做准备；
  
  
  
- __'./TestInfo__

  测试数据。

