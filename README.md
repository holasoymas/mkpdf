# Image to PDF Converter with Content Space

This script automates the process of converting images in a folder into a PDF, placing each image on a new page of an A4 document. It also ensures that there is space at the top of each page for additional content (e.g., text). The script adjusts the image sizes to fit within the page boundaries while preserving their aspect ratio.

## Features

- Convert all images (PNG files) in a specified folder to a PDF.
- Automatically resize images to fit within A4 page boundaries.
- Leave a configurable margin at the top of each page for content.
- Each image is placed at the bottom of the page to ensure space for content at the top.

## Requirements

To run the script, you need to install the required Python libraries. You can easily install them using the `requirements.txt` file provided.

### Installing Dependencies

1. Clone or download the repository.

2. Navigate to the project directory.

3. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

# Usage

1. Place all the images **(PNG files)** that you want to include in the PDF in a folder.

2. Modify the `image_folder` variable in the script to point to the folder containing your images, and adjust the `output_pdf` to specify the name of the resulting PDF file.

**_NOTE_** : **DONT FORGET TO CHANGE THE NAME OF VARIABLES**

```python
image_folder = "path/to/your/folder"  # Folder containing your PNG images
output_pdf = "output.pdf"  # Output PDF file name
```

3. Run the script:

```bash
python makepdf.py
```

This will generate a PDF with all the images from the specified folder.
