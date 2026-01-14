from ultralytics import YOLO
import multiprocessing

def main():
    # 1. 加载创新 P2 结构
    model = YOLO("yolo11-p2.yaml") 
    
    # 2. 加载预训练权重 (迁移学习加速收敛)
    try:
        model.load("yolo11n.pt")
        print("成功加载 yolo11n.pt 预训练权重")
    except Exception as e:
        print(f"权重加载警告: {e}")

    # 3. 开启 100 轮长跑 (稳定模式)
    print("开始 100 Epochs 训练... ")
    
    results = model.train(
        data="VisDrone.yaml",
        
        # === 核心修改 ===
        epochs=100,            
        project="runs/train",  # 保存路径
        name="p2_head_100_final", 
        # ===============
        
        imgsz=640,
        device=0,
        
        # === 稳定防崩配置 ===
        batch=4,       # 显存保护
        workers=0,     # 进程保护
        cache=False,   # 内存保护
        # ===========================
        
        exist_ok=True, # 如果名字重复允许覆盖
        amp=True,
        patience=0,    # 关闭早停 (Early Stopping)，强制跑满100轮
        cos_lr=True    # 开启余弦退火学习率，适合长周期训练，后期精度更高
    )

if __name__ == '__main__':
    multiprocessing.freeze_support()

    main()
