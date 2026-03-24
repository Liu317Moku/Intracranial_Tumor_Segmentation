import os
import shutil
import glob

#nU-Net 資料夾
task_dir = "/home/nnunet/nnUNet_raw/Dataset001" #改成自己的帳號名稱放置路徑中
imagesTr_dir = os.path.join(task_dir, "imagesTr")
labelsTr_dir = os.path.join(task_dir, "labelsTr")
imagesTs_dir = os.path.join(task_dir, "imagesTs")
os.makedirs(imagesTr_dir, exist_ok=True)
os.makedirs(labelsTr_dir, exist_ok=True)
os.makedirs(imagesTs_dir, exist_ok=True)

#原始影像與 mask 資料夾
src_images = "/home/train/med-ddpm/image" #改成自己的帳號名稱放置路徑中
src_masks = "/home/train/med-ddpm/mask" #改成自己的帳號名稱放置路徑中

# 找出所有影像檔
image_paths = sorted(glob.glob(os.path.join(src_images, "*")))
mask_paths = sorted(glob.glob(os.path.join(src_masks, "*")))

# 檢查數量一致
assert len(image_paths) == len(mask_paths), f"影像數量({len(image_paths)})與標註數量({len(mask_paths)})不一致！"

#  複製並重新命名
for idx, (img_path, mask_path) in enumerate(zip(image_paths, mask_paths)):
    case_id = f"seg_{idx:04d}"

    # nnU-Net 格式檔名
    new_img_name = f"{case_id}_0000.nii.gz"  # 影像加 _0000
    new_mask_name = f"{case_id}.nii.gz"      # mask 保留 case_id

    shutil.copy(img_path, os.path.join(imagesTr_dir, new_img_name))
    shutil.copy(mask_path, os.path.join(labelsTr_dir, new_mask_name))

print(f" 已完成轉換並複製 {len(image_paths)} 筆資料到 nnU-Net 格式資料夾：{task_dir}")
