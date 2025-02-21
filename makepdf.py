from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# Directory containing images
image_folder = "path/to/your/folder"
output_pdf = "output.pdf"
margin = 40  # Margin from the bottom and sides


def add_images_to_pdf(image_folder, output_pdf, margin=0):
    # A4 size in points (1 inch = 72 points)
    page_width, page_height = A4

    c = canvas.Canvas(output_pdf, pagesize=A4)

    # List of image files sorted by name
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".png")])

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)

        # Open image
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Convert image dimensions to points (assuming 72 DPI if not specified)
        img_width_pts = img_width * 72 / 96  # Assuming 96 DPI as a fallback
        img_height_pts = img_height * 72 / 96  # Assuming 96 DPI as a fallback

        # Resize image if it exceeds page boundaries
        if img_width_pts > (page_width - 2 * margin):
            scale_factor = (page_width - 2 * margin) / img_width_pts
            img_width_pts = page_width - 2 * margin
            img_height_pts = img_height_pts * scale_factor

        if img_height_pts > (page_height - 2 * margin):
            scale_factor = (page_height - 2 * margin) / img_height_pts
            img_height_pts = page_height - 2 * margin
            img_width_pts = img_width_pts * scale_factor

        # Calculate position to place image at the bottom
        x = (page_width - img_width_pts) / 2
        y = margin

        # Draw image
        c.drawImage(image_path, x, y, width=img_width_pts, height=img_height_pts)

        # Create a new page
        c.showPage()

    # Save the PDF
    c.save()


add_images_to_pdf(image_folder, output_pdf, margin)
