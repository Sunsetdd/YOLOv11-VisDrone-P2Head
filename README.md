# YOLOv11-VisDrone-P2Head
Improved YOLOv11 with P2-Head for Small Object Detection on VisDrone Dataset. (研究生课程论文代码：基于改进 YOLOv11 的无人机小目标检测)
# 基于改进 YOLOv11 的无人机视角下小目标检测研究
> Graduate Course Paper: Pattern Recognition and Computer Vision

## Abstract (摘要)
针对 VisDrone 数据集中微小目标检测精度低的问题，本项目提出了一种基于 YOLOv11n 的改进算法。通过引入针对 160×160 高分辨率特征图的 **P2 检测头 (P2-Head)**，显著增强了模型对极小像素目标的特征提取能力。
(这里可以把你论文的摘要粘贴过来)

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
