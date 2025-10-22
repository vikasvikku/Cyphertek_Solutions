import os
from glob import glob

# Change this to your dataset root folder
dataset_root = r"C:\Users\cyphe\Downloads\dataset.v2i.darknet"

splits = ["train", "test", "valid"]

for split in splits:
    folder = os.path.join(dataset_root, split)
    # Get all image files (jpg, png, etc.)
    image_files = glob(os.path.join(folder, ".jpg")) + glob(os.path.join(folder, ".png"))
    
    # Sort for consistency
    image_files.sort()
    
    # Output file (train.txt, test.txt, valid.txt)
    out_file = os.path.join(dataset_root, f"{split}.txt")
    
    with open(out_file, "w") as f:
        for img in image_files:
            f.write(img + "\n")
    
    print(f"{split}.txt created with {len(image_files)} entries at {out_file}")