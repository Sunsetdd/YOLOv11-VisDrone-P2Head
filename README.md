# YOLOv11-VisDrone-P2Head
Improved YOLOv11 with P2-Head for Small Object Detection on VisDrone Dataset. (研究生课程论文代码：基于改进 YOLOv11 的无人机小目标检测)
# 基于改进 YOLOv11 的无人机视角下小目标检测研究
> Graduate Course Paper: Pattern Recognition and Computer Vision

## Abstract (摘要)
无人机航拍图像具有视场宽广、背景复杂以及目标尺度极小等特点，导致传统目标检测算法在处理此类数据时容易出现特征丢失和漏检现象。针对VisDrone数据集中微小目标（如远处行人、密集车流）检测精度低的问题，本文提出了一种基于YOLOv11n的改进检测算法。该算法通过重构特征融合网络，引入了针对160×160高分辨率特征图的P2检测头（P2-Head），以增强模型对极小像素目标的特征提取能力。实验结果表明，在NVIDIA RTX 5060Ti硬件环境下，改进模型经过充分训练（100Epochs）后，整体性能及核心类别均显著优于基线模型。其中，行人（Pedestrian）和汽车（Car）的检测精度（mAP50）相比基线模型分别大幅提升了8.0%和5.4%，整体mAP50达到34.3%，反超基线4.7 个百分点。该研究充分验证了高分辨率 P2 特征层在解决无人机微小目标漏检问题上的卓越有效性。该研究验证了高分辨率特征层在无人机小目标检测任务中的有效性，为解决高空视角下的漏检问题提供了新的优化思路。


## Key Features (创新点)
- **P2 High-Resolution Head**: 新增 4倍下采样检测层，捕捉微小目标。
- **Feature Fusion**: 优化了 PANet 结构，缓解下采样带来的特征丢失。

## File Structure (文件说明)
- `train_ours.py`: 训练启动脚本
- `yolo11-p2.yaml`: 改进后的网络结构配置文件
- `best.pt`: 训练好的最佳权重文件

## Performance (实验结果)
| Model | mAP50 (All) | Pedestrian | Car |
| :--- | :---: | :---: | :---: |
| Baseline | 29.6% | 31.0% | 72.4% |
| **Ours (P2-Head)** | **34.3%** | **39.0%** | **77.8%** |

## Visualization (效果展示)
![Result](检测效果图 val_batch0_pred.jpg)
![val_batch0_pred](https://github.com/user-attachments/assets/460e7f6a-6aa5-40c0-a94d-635fa8134152)
