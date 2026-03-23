Intracranial Tumor Segmentation

Overview

This project focuses on 3D brain tumor segmentation on real clinical MRI data, handling unnormalized inputs and multiple tumor types. It is based on the nnUNet framework with a fine-tuning strategy to improve performance and generalization on diverse clinical cases.

Method

The model is built on nnUNet for 3D segmentation, with a fine-tuning strategy applied to transfer knowledge from synthetic data to real clinical data. The pipeline includes preprocessing steps such as resampling and intensity normalization, along with data augmentation techniques including rotation, flipping, and intensity scaling to improve robustness and generalization.

Results
<p align="center">
  <img width="805" height="341" alt="image" src="https://github.com/user-attachments/assets/e6fa0242-f8b2-475b-9a84-088b982d87f6" />
</p>
