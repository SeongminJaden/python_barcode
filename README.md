# python_barcode
# Barcode Scanner using OpenCV and gphoto2

This project captures an image using a connected camera via `gphoto2`, processes it using OpenCV, and decodes barcodes using `pyzbar`.

## Requirements

Ensure you have the following dependencies installed before running the script:

### System Requirements
- A camera supported by `gphoto2`
- Python 3.x
- OpenCV
- `gphoto2` (installed on your system)
- `pyzbar` for barcode detection

### Install Required Python Packages
```bash
pip install opencv-python pyzbar numpy
```

### Install gphoto2 (Linux/macOS)
```bash
sudo apt-get install gphoto2  # Ubuntu/Debian
yum install gphoto2  # CentOS/RHEL
brew install gphoto2  # macOS
```

## Usage

Run the following command to execute the script:
```bash
python main.py
```

## How It Works
1. The script captures an image from a connected camera using `gphoto2`.
2. The captured image is loaded using OpenCV.
3. The `pyzbar` library decodes any detected barcodes in the image.
4. If a barcode is found, it is outlined in the image, and its data is displayed.
5. The processed image is shown in a window.
6. The script prints the time taken for each processing step.

## Output
- The detected barcode data and its type are displayed in the console.
- The image with highlighted barcode regions is displayed in a window.

## Notes
- Make sure your camera is properly connected and recognized by `gphoto2`.
- The script will not work if `gphoto2` does not detect the camera.
- The barcode detection works best with clear and well-lit images.

## License
This project is open-source and available under the MIT License.
