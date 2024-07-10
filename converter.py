import os
from PIL import Image

def convert_to_svg_with_inkscape(input_image_path, output_svg_path):
    # Ensure the image is in a format Inkscape can use
    png_image_path = input_image_path.rsplit('.', 1)[0] + '_temp.png'
    image = Image.open(input_image_path)
    image.save(png_image_path, 'PNG')

    # Use Inkscape's command-line interface to convert PNG to SVG
    os.system(f'inkscape {png_image_path} --export-plain-svg={output_svg_path}')

    # Clean up the intermediate PNG file
    os.remove(png_image_path)

input_image_path = 'fig1.png'
output_svg_path = 'fig1.svg'

convert_to_svg_with_inkscape(input_image_path, output_svg_path)
print(f"Conversion of {input_image_path} completed.")

input_image_path = 'fig2.png'
output_svg_path = 'fig2.svg'

convert_to_svg_with_inkscape(input_image_path, output_svg_path)
print(f"Conversion of {input_image_path} completed.")
