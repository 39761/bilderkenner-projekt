import torch
import tensorflow as tf
import cv2

print("PyTorch:", torch.__version__)
print("TensorFlow:", tf.__version__)
print("OpenCV:", cv2.__version__)

print("CUDA verfügbar (Torch):", torch.cuda.is_available())
