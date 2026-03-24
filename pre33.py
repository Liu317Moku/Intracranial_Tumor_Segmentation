import os
import json
import glob
import nibabel as nib
import numpy as np
import subprocess
import shutil

# 路徑設定
task_dir = "/home/nnunet/nnUNet_raw/Dataset001"
imagesTr_dir = os.path.join(task_dir, "imagesTr")
labelsTr_dir = os.path.join(task_dir, "labelsTr")
backup_dir = labelsTr_dir + "_backup"

# 先備份原 labelsTr
if not os.path.exists(backup_dir):
    shutil.copytree(labelsTr_dir, backup_dir)
    print(f" 原 labelsTr 已備份到 {backup_dir}")
else:
    print(" 已存在 labelsTr_backup，略過備份")

# 覆蓋 labelsTr：0,1 → 0；2 → 1
label_files = sorted(glob.glob(os.path.join(labelsTr_dir, "*.nii.gz")))
print(f" 找到 {len(label_files)} 個標籤檔，轉為 tumor-only")

for lbl_path in label_files:
    img = nib.load(lbl_path)

    # 關鍵：轉成整數
    data = img.get_fdata().astype(np.int16)

    unique_before = np.unique(data)

    new_data = np.zeros_like(data, dtype=np.uint8)
    new_data[data == 2] = 1

    unique_after = np.unique(new_data)

    print(
        f"{os.path.basename(lbl_path)} | "
        f"before: {unique_before} -> after: {unique_after}"
    )

    if 1 not in unique_after:
        print(f"  警告：{os.path.basename(lbl_path)} 轉換後沒有腫瘤")

    new_img = nib.Nifti1Image(new_data, img.affine, img.header)
    nib.save(new_img, lbl_path)

print(" labelsTr 已轉為二分類（0=背景, 1=腫瘤）")

image_files = sorted(glob.glob(os.path.join(imagesTr_dir, "*.nii.gz")))

dataset_json = {
    "name": "Dataset001_TumorOnly",
    "description": "Tumor segmentation only",
    "tensorImageSize": "3D",
    "channel_names": {"0": "image"},
    "labels": {
        "background": 0,
        "tumor": 1
    },
    "numTraining": len(image_files),
    "numTest": 0,
    "file_ending": ".nii.gz",
    "training": [
        {
            "image": os.path.join("imagesTr", os.path.basename(img)),
            "label": os.path.join("labelsTr", os.path.basename(img))
        }
        for img in image_files
    ],
    "test": []
}

dataset_json_path = os.path.join(task_dir, "dataset.json")
with open(dataset_json_path, "w", encoding="utf-8") as f:
    json.dump(dataset_json, f, indent=4)

print(" dataset.json 已更新")

#nnU-Net 環境變數
os.environ["nnUNet_raw"] = "/home/u20030317/twcc1/nnunet/nnUNet_raw"
os.environ["nnUNet_preprocessed"] = "/home/u20030317/twcc1/nnunet/nnUNet_preprocessed"
os.environ["nnUNet_results"] = "/home/u20030317/twcc1/nnunet/nnUNet_results"

# 重新 preprocess（必須）
cmd = [
    "/home/u20030317/miniconda3/envs/nnunet4/bin/nnUNetv2_plan_and_preprocess",
    "-d", "1",
    "--verify_dataset_integrity"
]

print(" 開始 nnU-Net 預處理（tumor only）...")
subprocess.run(cmd, check=True)
print(" nnU-Net 預處理完成")
