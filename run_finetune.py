import os

# 環境變數
os.environ["nnUNet_raw_data_base"] = "/home/u20030317/twcc1/nnunet/nnUNet_raw"
os.environ["nnUNet_preprocessed"] = "/home/u20030317/twcc1/nnunet/nnUNet_preprocessed"
os.environ["nnUNet_results"] = "/home/u20030317/twcc1/nnunet/nnUNet_results"

from nnunetv2.training.network_training.nnUNet_training import train_nnUNet

# 執行 fine-tune
train_nnUNet(
    trainer_class_name="nnUNetTrainer_20epochs_finetune",  # 你的 Trainer class
    dataset_name_or_id="Dataset001",                        # 保留原資料名稱
    fold=0,                                                 # 你要訓練的 fold
    configuration="3d_fullres"                              # 3D full resolution
)
