# 6. 推論 (Inference)

import os
import subprocess

# 1. GPU 設定
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # 指定 GPU

# 2. nnU-Net 環境變數
os.environ['nnUNet_raw'] = '/home/u20030317/twcc1/nnunet/nnUNet_raw'
os.environ['nnUNet_preprocessed'] = '/home/u20030317/twcc1/nnunet/nnUNet_preprocessed'
os.environ['nnUNet_results'] = '/home/u20030317/twcc1/nnunet/nnUNet_results'

nnUNet_raw = os.environ['nnUNet_raw']

#3. 推論資料夾
input_folder = os.path.join(nnUNet_raw, "Dataset001", "imagesTs")
output_folder = "nnUNet_predictions"

os.makedirs(output_folder, exist_ok=True)

print("CUDA_VISIBLE_DEVICES =", os.environ["CUDA_VISIBLE_DEVICES"])
print("Input folder:", input_folder)
print("Output folder:", output_folder)

# 4. nnUNetv2_predict 指令
cmd = [
    "/home/u20030317/miniconda3/envs/nnunet4/bin/nnUNetv2_predict",
    "-d", "1",
    "-i", input_folder,
    "-o", output_folder,
    "-tr", "nnUNetTrainer_10epochs",
    "-c", "3d_fullres",
    "-f", "0"
]

# 5. 執行推論
subprocess.run(cmd, check=True)

print("✅ 推論完成，結果存於：", output_folder)
