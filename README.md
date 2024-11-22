# ImageFormatConverter

A lightweight Python utility for converting images between different formats while handling transparency and color modes appropriately.

## Features

- Converts images between various formats (PNG, JPEG, WEBP, etc.)
- Handles RGBA to RGB conversion for JPEG output
- Preserves original image quality
- Maintains directory structure
- Simple, single-function implementation

## Requirements

- Python 3.6+
- Pillow (PIL)

## Installation

```bash
pip install Pillow
```

## Usage

```python
from image_format_converter import convert_image

# Convert a WEBP image to PNG
converted_path = convert_image("image.webp", "PNG")

# Convert a PNG image to JPEG
converted_path = convert_image("image.png", "JPEG")
```

## Function Parameters

- `input_path`: Path to the input image file
- `output_format`: Desired output format (e.g., "PNG", "JPEG", "WEBP")

Returns the path to the converted image.

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
