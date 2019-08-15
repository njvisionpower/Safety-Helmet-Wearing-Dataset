# SafetyHelmetWearing-Dataset
Safety helmet wearing and head detect dataset, with pretrained model    

## Introduction
This repo provide the dataset which can be used for both safety helmet wearing and head detection. It includes 7581 images with 9044 human safety helmet wearing objects and 111514 normal head(not wearing) objects. The safety helmet wearing images comes from goolge or baidu and we manually label with LabelImg. Some of normal head got from [SCUT-HEAD](https://github.com/HCIILAB/SCUT-HEAD-Dataset-Release). I fixed some bugs on original SCUT-HEAD exists bugs to make it can be directly loaded as normal Pascal VOC format. Also we provide some pretrained models with MXNet gluoncv.    

<p align="center"> 
<img src="https://github.com/njvisionpower/SafetyHelmetWearing-Dataset/blob/master/demo1.jpg" width = 80% height = 80%>
</p>  

## Download
[BaiduDrive](https://pan.baidu.com/s/19GcMnmdmC1RpSpFJisRTFQ)
[GoogleDrive](https://pan.baidu.com/s/19GcMnmdmC1RpSpFJisRTFQ)
### How to use
We annotate the data as VOC format:  

```
---VOC2028    
    ---Annotations    
    ---ImageSets    
    ---JPEGImages   
```
There are two object class names, hat for safety hemlet wearing object and person for normal head.    
