# SafetyHelmetWearing-Dataset(安全帽佩戴检测数据集)
Safety helmet (hardhat) wearing detect dataset(安全帽佩戴检测数据集, SHWD). We also provide pretrained models.

## Introduction
SHWD provide the dataset used for both safety helmet wearing and human head detection. It includes 7581 images with 9044 human safety helmet wearing objects(positive) and 111514 normal head objects(not wearing or negative). The positive objects got from goolge or baidu, and we manually labeld with LabelImg. Some of negative objects got from [SCUT-HEAD](https://github.com/HCIILAB/SCUT-HEAD-Dataset-Release). We fixed some bugs for original SCUT-HEAD and make the data can be directly loaded as normal Pascal VOC format. Also we provide some pretrained models with MXNet GluonCV.    

<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/demo1.jpg" width = 70% height = 70%>
</p>  

## Dataset and model download
### Dataset
[BaiduDrive](https://pan.baidu.com/s/19GcMnmdmC1RpSpFJisRTFQ)
[GoogleDrive](https://drive.google.com/open?id=1qWm7rrwvjAWs1slymbrLaCf7Q-wnGLEX)
### Model
[BaiduDrive](https://pan.baidu.com/s/1dWNU_q59sw1a3TVtV7VXEg)
### Benchmark
model | darknet | mobile1.0 |  mobile0.25
--------- | ------------- | ------------- | ------------- 
map   |  88.5 |  86.3 |  75.0

## How to use dataset
We annotate the data as Pascal VOC format:  
```
---VOC2028    
    ---Annotations    
    ---ImageSets    
    ---JPEGImages   
```
Two object class names for the task, "hat" for positive object and "person" for negative object.
## How to run
### Dependency
Make sure you install MXNet, GluonCV, OpenCV
### Test with pretrained models
Two way to inference. 
#### First way
```
1. Download models from link (https://pan.baidu.com/s/1dWNU_q59sw1a3TVtV7VXEg).  
2. Run "python test_yolo.py" with default settings, or change options:  
--network: darknet/mobile1.0/mobile0.25 network, default darknet53;  
--threshold: confidence that filter object;  
--gpu: use gpu or cpu, default gpu;  
--short: short side input size for original image.
```
#### Second way, inference with mxnet symbol
Download models from [Symbol](https://pan.baidu.com/s/1EEdsjECJy_y00dekRre0eA), then inference with symbol:
```
python test_symbol.py
```
### Notice
**1.** This repo provide 3 yolo models with different size, default darknet53.  
**2.** Parameter "short" means the input size of short side for original image, you can try larger value if want to detect dense objects or big size image.  
**3.** Hyper-parameter threshold means the confidence for detect, change it for different task.  

## How to train
You can see function "get_dataset" in the file "train_yolo.py" to set dataset path. An example, download dataset and unzip to the path such as "D:\VOCdevkit\VOC2028", train/val dataset can set as:
```
train_dataset = VOCLike(root='D:\VOCdevkit', splits=[(2028, 'trainval')])
val_dataset = VOCLike(root='D:\VOCdevkit', splits=[(2028, 'test')])
```
Then check train_yolo.py to set options and train, such as:
```
python train_yolo.py --batch-size 4 -j 4 --warmup-epochs 3
```
### Notice
**1.** One common problem when train yolo is gradient explosion, try more epoches to warmup or use smaller learning rate.  
**2.** Much time spent on dataset loading with CPU, set "-j" number bigger if you have multi-core CPU and will improve train speed.  
**3.** If train on Windows, sometimes program may blocked, see https://discuss.gluon.ai/t/topic/9388/11, if train on Linux make sure you have enough share memory.
## Demo
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/3_result.jpg" width = 50% height = 50%>
</p>  
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/4_result.jpg" width = 50% height = 50%>
</p> 
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/5_result.jpg" width = 50% height = 50%>
</p> 
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/6_result.jpg" width = 50% height = 50%>
</p> 
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/7_result.jpg" width = 50% height = 50%>
</p> 
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/8_result.jpg" width = 50% height = 50%>
</p> 
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/1_result.jpg" width = 50% height = 50%>
</p>  
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/2_result.jpg" width = 50% height = 50%>
</p> 
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/9_result.jpg" width = 50% height = 50%>
</p> 
<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/image/10_result.jpg" width = 50% height = 50%>
</p> 
