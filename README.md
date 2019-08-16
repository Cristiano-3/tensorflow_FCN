# FCN/UNet In Action

## Folders Introduction

- dataset: 存放数据集及其处理代码(读取, 转换, 预处理)
  - data 数据存储

- deploy: 部署相关代码
  - models 存储模型文件
  - save_model.py 导出部署用的模型文件
  - client.py 服务测试客户端

- experiments: 实验参数, 日志, 脚本
  - cfgs 参数文件
  - logs 实验日志
  - scripts 实验脚本

- lib: 项目主代码
  - nets: 网络代码
  - utils: 模型工具代码

- pretrained: 预训练模型

- output: 存放训练 checkpoints

- tools: 存放通用工具代码

train.py 训练  
inference.py 推断  
eval.py 测试评估  
demo.py 展示  

## Requirements

## Training
