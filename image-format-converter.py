from PIL import Image
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def convert_image(input_path, output_format):
    with Image.open(input_path) as img:
        if output_format.upper() == 'JPEG' and img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        output_path = input_path.rsplit('.', 1)[0] + '.' + output_format.lower()
        img.save(output_path)
        return output_path

# Example usage:
input_path = "your_image_filename.webp"  # Change this to your image path
output_format = "PNG"           # Change this to your desired format
converted_path = convert_image(input_path, output_format)
