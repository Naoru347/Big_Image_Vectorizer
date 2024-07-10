
# Image to SVG Conversion Script

This script converts a JPG or PNG image to an SVG format using Inkscape for vectorization. 

## Prerequisites

- **Python 3.x**
- **Pillow** and **cairosvg** Python libraries
- **Inkscape** installed on your system

## Installation

### 1. Install Python Libraries

First, ensure you have Python installed. Then, install the required Python libraries using `pip`.

```bash
pip install pillow cairosvg
```

### 2. Install Inkscape

#### On macOS:
Install Inkscape using Homebrew:

```bash
brew install inkscape
```

#### On Linux:
Install Inkscape using your package manager. For example, on Ubuntu:

```bash
sudo apt-get install inkscape
```

#### On Windows:
Download and install Inkscape from the [official website](https://inkscape.org/release/).

## Usage

1. Ensure you have your input image in the same directory as the script, or provide the correct path to the image.

2. Run the script:

```bash
python convert_to_svg.py
```

### Script Explanation

The script performs the following steps:

1. **Check and Install Packages**: Ensures that `Pillow` and `cairosvg` libraries are installed.
2. **Convert Image to PNG**: Converts the input image to a temporary PNG file.
3. **Convert PNG to SVG**: Uses Inkscape to convert the PNG file to SVG format.
4. **Clean Up**: Removes the temporary PNG file.

### convert_to_svg.py

```python
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

def main():
    input_image_path = 'input_image.png'
    output_svg_path = 'output_image.svg'

    if not os.path.exists(input_image_path):
        print(f"Input file {input_image_path} does not exist.")
        return
    
    convert_to_svg_with_inkscape(input_image_path, output_svg_path)
    print("Conversion completed.")

if __name__ == "__main__":
    main()
```

## Troubleshooting

### Inkscape Command Not Found

If you encounter an error that the `inkscape` command is not found, ensure that Inkscape is installed and available in your system's PATH. You can check this by running:

```bash
inkscape --version
```

If the command is not found, add Inkscape to your PATH or specify the full path to the `inkscape` executable in the script.

## License

This project is licensed under the MIT License.
