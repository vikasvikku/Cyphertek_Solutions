import os
import yaml

# Path to your Roboflow dataset
dataset_path = r"C:\Users\cyphe\Downloads\dataset.v2i.darknet"

# Path to data.yaml (YOLOv5/YOLOv8 style)
yaml_file = os.path.join(dataset_path, "data.yaml")

# Load data.yaml
with open(yaml_file, "r") as f:
    data = yaml.safe_load(f)

# Extract class names and number of classes
class_names = data["names"]
num_classes = data["nc"]

# --- Create obj.names ---
obj_names_path = os.path.join(dataset_path, "obj.names")
with open(obj_names_path, "w") as f:
    for name in class_names:
        f.write(name + "\n")
print(f"✅ Created: {obj_names_path}")

# --- Create obj.data ---
obj_data_path = os.path.join(dataset_path, "obj.data")
with open(obj_data_path, "w") as f:
    f.write(f"classes={num_classes}\n")
    f.write("train=data/train.txt\n")
    f.write("valid=data/valid.txt\n")
    f.write("names=data/obj.names\n")
    f.write("backup=backup/\n")
print(f"✅ Created: {obj_data_path}")

# --- Create train.txt / valid.txt / test.txt ---
splits = {"train": data["train"], "valid": data["val"], "test": data.get("test", None)}

for split, split_path in splits.items():
    if split_path is None:
        continue

    # Absolute path to images folder
    split_abs_path = os.path.join(dataset_path, split, "images")

    # File to save image paths
    txt_file = os.path.join(dataset_path, f"{split}.txt")

    with open(txt_file, "w") as f:
        for img in os.listdir(split_abs_path):
            if img.endswith(".jpg") or img.endswith(".png"):
                abs_img_path = os.path.join(split_abs_path, img)
                f.write(abs_img_path + "\n")
    print(f"✅ Created: {txt_file}")

print("🎉 Conversion complete! Now you have obj.names, obj.data, train.txt, valid.txt, test.txt")