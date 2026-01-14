from ultralytics import YOLO
import os
import random
import cv2

# ================= 配置区域 =================
# 最佳权重文件路径
model_path = r"D:\Documents\Desktop\UAV_SmallObject_Detection\runs\train\p2_head_innovation\weights\best.pt"

# 2. 验证集图片的路径 (随机抽一张测试)
source_image_dir = r"D:\Documents\Desktop\UAV_SmallObject_Detection\datasets\VisDrone2019-DET-val\images"

# 3. 结果保存路径
save_dir = "inference_results"
# ===========================================

def main():
    # 1. 加载训练好的改进模型
    print(f"正在加载模型: {model_path} ...")
    model = YOLO(model_path)

    # 2. 从验证集中随机挑一张图
    all_images = [f for f in os.listdir(source_image_dir) if f.endswith('.jpg')]
    if not all_images:
        print(" 找不到图片，请检查 source_image_dir 路径")
        return
    
    selected_img = random.choice(all_images)
    img_path = os.path.join(source_image_dir, selected_img)
    print(f" 正在推理图片: {selected_img}")

    # 3. 进行推理 (Predict)
    # conf=0.25 表示置信度大于 25% 的才画框
    # save=True 自动保存结果
    results = model.predict(source=img_path, conf=0.25, save=True, project=save_dir, name="demo")

    print(f" 推理完成！结果已保存到: {results[0].save_dir}")

if __name__ == "__main__":
    main()