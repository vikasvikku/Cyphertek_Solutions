# Updated Image Augmentation Tool

## Features
- Simple function-based approach
- Converts any image to 416×416 grayscale
- Creates 30 identical copies (no rotation/augmentation)
- Uses original filename with numbering
- PyTorch tensor conversion included

## Usage

1. Update the image path in the script:
   ```python
   image_path = r"C:\path\to\your\image.jpg"
   ```

2. Run the script:
   ```bash
   python updated_augment.py
   ```

## Configuration
Modify these variables in the script:
- `image_path`: Path to your input image
- `output_folder`: Output directory (default: "Annotated_images")
- `num_copies`: Number of copies to create (default: 30)
- `size`: Output image size (default: (416, 416))

## Function Parameters
```python
save_copies(image_path, output_folder, num_copies=30, size=(416, 416))
```

## Output
- Files named: `filename_01.png`, `filename_02.png`, etc.
- All images resized to 416×416 pixels
- Grayscale format
- No rotation - exact copies only
- Spaces in filename replaced with underscores