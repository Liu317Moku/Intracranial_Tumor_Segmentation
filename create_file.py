import os

# 設定 nnU-Net 資料夾路徑
base_dir = "nnunet"
nnUNet_raw = os.path.join(base_dir, "nnUNet_raw")
nnUNet_preprocessed = os.path.join(base_dir, "nnUNet_preprocessed")
nnUNet_results = os.path.join(base_dir, "nnUNet_results")

# 建立資料夾
os.makedirs(nnUNet_raw, exist_ok=True)
os.makedirs(nnUNet_preprocessed, exist_ok=True)
os.makedirs(nnUNet_results, exist_ok=True)

# 設定環境變數
os.environ["nnUNet_raw"] = nnUNet_raw
os.environ["nnUNet_preprocessed"] = nnUNet_preprocessed
os.environ["nnUNet_results"] = nnUNet_results

print("nnU-Net 資料夾已建立")