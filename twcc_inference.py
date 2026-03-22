#6. 推論 (Inference) - best checkpoint + fold0 + TTA

import os
import subprocess

#GPU 設定
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

#nnU-Net 環境變數
os.environ['nnUNet_raw'] = '/home/u20030317/twcc1/nnunet/nnUNet_raw'
os.environ['nnUNet_preprocessed'] = '/home/u20030317/twcc1/nnunet/nnUNet_preprocessed'
os.environ['nnUNet_results'] = '/home/u20030317/twcc1/nnunet/nnUNet_results'

#推論資料夾
input_folder = "/home/u20030317/twcc1/private/INPUT"
output_folder = "/home/u20030317/twcc1/private/PREDICT"

os.makedirs(output_folder, exist_ok=True)

print("CUDA_VISIBLE_DEVICES =", os.environ["CUDA_VISIBLE_DEVICES"])
print("Input folder:", input_folder)
print("Output folder:", output_folder)

#nnUNetv2_predict 指令
cmd = [
    "/home/u20030317/miniconda3/envs/nnunet4/bin/nnUNetv2_predict",
    "-d", "1",  # dataset ID
    "-i", input_folder,
    "-o", output_folder,
    "-tr", "nnUNetTrainer_50epochs",  # 你自訂 trainer
    "-c", "3d_fullres",
    "-f", "0",  # fold0
    "-chk", "checkpoint_best.pth",
    #  開啟 TTA，不加 --disable_tta
]

# 執行推論
print("開始推論（best checkpoint + fold0 + TTA）...")
subprocess.run(cmd, check=True)
print("推論完成，結果存於：", output_folder)
