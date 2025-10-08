import cv2
import os
import torch
import random
import numpy as np

def augment_and_save(image_path, output_folder, num_copies=30, size=(416, 416), max_angle=4):
    os.makedirs(output_folder, exist_ok=True)


    base_name = os.path.splitext(os.path.basename(image_path))[0]


    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Image not found or unable to load.")


    img = cv2.resize(img, size)
    h, w = img.shape[:2]
    center = (w // 2, h // 2)

    for i in range(num_copies): 
        angle = random.uniform(-max_angle, max_angle)

        
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

        
        tensor_img = torch.from_numpy(rotated).unsqueeze(0).float() / 255.0
        save_path = os.path.join(output_folder, f"{base_name}_{i+1:02d}.png")
        cv2.imwrite(save_path, rotated)

        print(f"Saved: {save_path} | Angle: {angle:.2f}°")


image_path = r"C:\Users\vikas\Downloads\images\images\Segment_G_LED1.png" 
output_folder = "Annotated_images_oct8"
augment_and_save(image_path, output_folder)
