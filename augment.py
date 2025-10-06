import cv2
import os
import torch
import random
import numpy as np

def augment_and_save(image_path, output_folder, num_copies=30, size=(416, 416), max_angle=4):
    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Extract base filename (without extension)
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    # Load grayscale image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Image not found or unable to load.")

    # Resize to required size
    img = cv2.resize(img, size)
    h, w = img.shape[:2]
    center = (w // 2, h // 2)

    for i in range(num_copies):
        # Always restrict angle within ±max_angle (≤4°)
        angle = random.uniform(-max_angle, max_angle)

        # Rotate image
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

        # Convert to PyTorch tensor (1, H, W) and normalize [0,1]
        tensor_img = torch.from_numpy(rotated).unsqueeze(0).float() / 255.0

        # Save rotated copy with unique name (bill_01.png, bill_02.png ...)
        save_path = os.path.join(output_folder, f"{base_name}_{i+1:02d}.png")
        cv2.imwrite(save_path, rotated)

        print(f"Saved: {save_path} | Angle: {angle:.2f}°")

# Example usage
image_path = r"C:\Users\vikas\Downloads\images\images\Segment B.jpg"  # change path if needed
output_folder = "Annotated_images"
augment_and_save(image_path, output_folder)
