# QR Code Generator

A simple Python tool to generate QR codes for various types of content, with support for basic, styled, and logo-embedded QR codes.

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Usage

#### Basic QR Code
```bash
python qr_code_generator.py "https://example.com" -o my_qr.png
```

#### Styled QR Code (with rounded corners and gradient)
```bash
python qr_code_generator.py "https://example.com" --styled -o styled_qr.png
```

#### QR Code with Logo
```bash
python qr_code_generator.py "https://example.com" --logo logo.png -o qr_with_logo.png
```

#### Multiple QR Codes
```bash
python qr_code_generator.py "https://site1.com,https://site2.com,https://site3.com" --multiple
```

#### Interactive Mode
```bash
python qr_code_generator.py
```

### Programmatic Usage

```python
from qr_code_generator import generate_basic_qr, generate_styled_qr

# Generate basic QR code
generate_basic_qr("https://example.com", "output.png")

# Generate styled QR code
generate_styled_qr("https://example.com", "styled_output.png")
```

## Examples

Run the example script to generate QR codes for the Quaker Scientists project:

```bash
python example_qr_codes.py
```

This will create QR codes for:
- Wikipedia pages of the three main scientists
- Project repository URL
- Knowledge graph visualization
- Contact information (vCard format)

## Features

- **Basic QR Codes**: Simple black and white QR codes
- **Styled QR Codes**: Rounded corners with gradient colors
- **Logo Integration**: Embed logos in the center of QR codes
- **Multiple Generation**: Create multiple QR codes from a list
- **Interactive Mode**: User-friendly command-line interface
- **Customizable**: Adjustable size, border, and error correction

## File Structure

```
qr_code_generator.py     # Main QR code generator script
example_qr_codes.py      # Example usage for Quaker Scientists project
requirements.txt         # Python dependencies
QR_CODE_README.md        # This documentation
qr_codes/               # Directory for generated QR codes (created automatically)
```

## Error Correction Levels

The generator uses different error correction levels:
- **Basic QR codes**: Low error correction (L)
- **Logo-embedded QR codes**: High error correction (H) to accommodate the logo

## Tips

1. **Logo Size**: Keep logos small (about 1/4 the size of the QR code) for best results
2. **Error Correction**: Higher error correction allows for larger logos but increases QR code size
3. **Testing**: Always test QR codes with multiple devices to ensure readability
4. **File Formats**: All QR codes are saved as PNG files for maximum compatibility


