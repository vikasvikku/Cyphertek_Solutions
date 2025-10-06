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
- <10% images with ≤4° rotation
- Remaining images with up to ±10° rotation
- Handles grayscale images