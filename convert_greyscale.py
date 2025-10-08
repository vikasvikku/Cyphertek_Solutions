import torch
from torchvision import transforms
from PIL import Image
import os

def convert_to_greyscale(image_path, output_path="output_greyscale.png"):
    # Check if image exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at: {image_path}")

    # Open the image
    img = Image.open(image_path).convert("RGB")

    # Convert image to tensor
    transform_to_tensor = transforms.ToTensor()
    img_tensor = transform_to_tensor(img)

    # Convert to grayscale using standard luminance formula
    weights = torch.tensor([0.2989, 0.5870, 0.1140]).view(3, 1, 1)
    grey_tensor = torch.sum(img_tensor * weights, dim=0, keepdim=True)

    # Convert back to PIL image
    transform_to_pil = transforms.ToPILImage()
    grey_img = transform_to_pil(grey_tensor)

    # Save output
    grey_img.save(output_path)
    print(f"✅ Grayscale image saved successfully: {output_path}")

if __name__ == "__main__":
    # 🔧 Just change this path to your input image
    image_path = r"C:\Users\vikas\Downloads\images\segment_f_and_led1.png"  # ⬅️ paste your image path here
    output_path = "Segment_F_LED1.png"  # name of the output image

    convert_to_greyscale(image_path, output_path)
