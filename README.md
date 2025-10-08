# Image Augmentation Tool

## Requirements
- Python 3.7+
- OpenCV (opencv-python)
- PyTorch
- NumPy

## Setup Environment

1. Run the setup script:
   ```
   setup_env.bat
   ```

2. Or manually:
   ```
   python -m venv venv
   call venv\Scripts\activate.bat
   pip install -r requirements.txt
   ```

## Usage
1. Activate environment: `call venv\Scripts\activate.bat`
2. Update image path in `augment.py`
3. Run: `python augment.py`

## Features
- Resizes images to 416x416
- Creates 30 augmented copies
- Random rotation up to ±4° for all images
- Uses original filename with numbering
- Handles grayscale images
- PyTorch tensor conversion included

## Configuration
Modify these variables in `augment.py`:
- `image_path`: Path to input image
- `output_folder`: Output directory
- `num_copies`: Number of copies (default: 30)
- `max_angle`: Maximum rotation angle (default: 4°)

## Output
- Files named: `filename_01.png`, `filename_02.png`, etc.
- All images 416×416 grayscale
- Random rotations within ±4°