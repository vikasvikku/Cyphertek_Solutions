import cv2
import os
import torch
import numpy as np

def save_copies(image_path, output_folder, num_copies=30, size=(416, 416)):
    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    
    base_name = os.path.splitext(os.path.basename(image_path))[0].replace(" ", "_")

    # Load grayscale image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Image not found or unable to load.")

    
    img = cv2.resize(img, size)

    
    tensor_img = torch.from_numpy(img).unsqueeze(0).float() / 255.0

    
    for i in range(num_copies):
        save_path = os.path.join(output_folder, f"{base_name}_{i+1:02d}.png")
        cv2.imwrite(save_path, img)
        print(f"Saved: {save_path}")


image_path = r"C:\Users\vikas\Downloads\images\images\Segment B.jpg"  
output_folder = "Annotated_images"
save_copies(image_path, output_folder)
