# SafetyHelmetWearing-Dataset(安全帽佩戴检测数据集)
SHWD, Safety helmet wearing and head detect dataset(安全帽佩戴检测数据集), with pretrained model   

## Introduction
SHWD provide the dataset used for both safety helmet wearing and human head detection. It includes 7581 images with 9044 human safety helmet wearing objects(positive) and 111514 normal head objects(not wearing or negative). The positive objects comes from goolge or baidu and we manually label with LabelImg. Some of negative objects got from [SCUT-HEAD](https://github.com/HCIILAB/SCUT-HEAD-Dataset-Release). I fixed some bugs for original SCUT-HEAD and make the data can be directly loaded as normal Pascal VOC format. Also we provide some pretrained models with MXNet GluonCV.    

<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/demo1.jpg" width = 70% height = 70%>
</p>  

## Download
[BaiduDrive](https://pan.baidu.com/s/19GcMnmdmC1RpSpFJisRTFQ)
[GoogleDrive](https://drive.google.com/open?id=1qWm7rrwvjAWs1slymbrLaCf7Q-wnGLEX)
## How to use
We annotate the data as VOC format:  

```
---VOC2028    
    ---Annotations    
    ---ImageSets    
    ---JPEGImages   
```
There are two object class names, hat for safety hemlet wearing object and person for normal head.
## How to run
### Dependency
MXNet, GluonCV, OpenCV
### Run
Run "python test_yolo.py" with default settings.   
### Notice
**1** This repo provide 3 yolo models with different size, default darknet53.  
**2** Parameter "short" means the input size of short side for original image, you can try larger value if want to detect dense objects or big size image.  
**3** Hyper-parameter threshold means the confidence for detect, change it for different task.  
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
