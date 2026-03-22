import os
import subprocess

#  GPU 設定
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

#  關鍵：關閉 torch.compile / triton
os.environ["NNUNET_DISABLE_COMPILE"] = "1"
os.environ["TORCHINDUCTOR_DISABLE_TRITON"] = "1"
os.environ["TORCH_COMPILE"] = "0"        # 保險
os.environ["TORCHDYNAMO_DISABLE"] = "1"  # 保險

#  nnU-Net 路徑設定
os.environ["nnUNet_raw"] = "/home/u20030317/twcc1/nnunet/nnUNet_raw"
os.environ["nnUNet_preprocessed"] = "/home/u20030317/twcc1/nnunet/nnUNet_preprocessed"
os.environ["nnUNet_results"] = "/home/u20030317/twcc1/nnunet/nnUNet_results"

# （可留可不留，不影響）
os.environ["CC"] = "/home/u20030317/miniconda3/envs/nnunet4/bin/x86_64-conda-linux-gnu-gcc"
os.environ["CXX"] = "/home/u20030317/miniconda3/envs/nnunet4/bin/x86_64-conda-linux-gnu-g++"
os.environ["LD_LIBRARY_PATH"] = (
    "/home/u20030317/miniconda3/envs/nnunet4/lib:" +
    os.environ.get("LD_LIBRARY_PATH", "")
)

print(f" 使用 GPU: {os.environ['CUDA_VISIBLE_DEVICES']}")
print(" torch.compile / triton 已停用")

#  nnU-Net v2 訓練指令
cmd = [
    "/home/u20030317/miniconda3/envs/nnunet4/bin/nnUNetv2_train",
    "Dataset001",
    "3d_fullres",
    "0",
    "-tr", "nnUNetTrainer_50epochs"
]

print(" 開始 nnU-Net 訓練...")
subprocess.run(cmd, check=True)
print(" nnU-Net 訓練完成")



