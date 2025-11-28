#!/usr/bin/env python3
"""
QR Code Generator
A simple tool to generate QR codes for various types of content.
"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import argparse
import os
from PIL import Image, ImageDraw, ImageFont
import sys

def generate_basic_qr(data, filename="qrcode.png", size=10, border=4):
    """Generate a basic QR code"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"Basic QR code saved as: {filename}")
    return filename

def generate_styled_qr(data, filename="styled_qrcode.png", size=10, border=4):
    """Generate a styled QR code with rounded corners and gradient"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(back_color=(255, 255, 255), center_color=(70, 130, 180), edge_color=(25, 25, 112))
    )
    img.save(filename)
    print(f"Styled QR code saved as: {filename}")
    return filename

def generate_qr_with_logo(data, logo_path, filename="qrcode_with_logo.png", size=10, border=4):
    """Generate a QR code with a logo in the center"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create QR code
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Load and resize logo
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        logo_size = qr_img.size[0] // 4  # Logo should be 1/4 of QR code size
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Calculate position to center the logo
        logo_pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
        
        # Paste logo onto QR code
        qr_img.paste(logo, logo_pos)
        qr_img.save(filename)
        print(f"QR code with logo saved as: {filename}")
    else:
        print(f"Logo file not found: {logo_path}")
        return generate_basic_qr(data, filename)
    
    return filename

def generate_multiple_qrs(data_list, prefix="qr", size=10, border=4):
    """Generate multiple QR codes from a list of data"""
    generated_files = []
    for i, data in enumerate(data_list):
        filename = f"{prefix}_{i+1}.png"
        generate_basic_qr(data, filename, size, border)
        generated_files.append(filename)
    return generated_files

def main():
    parser = argparse.ArgumentParser(description='Generate QR codes')
    parser.add_argument('data', help='Data to encode in QR code')
    parser.add_argument('-o', '--output', default='qrcode.png', help='Output filename')
    parser.add_argument('-s', '--size', type=int, default=10, help='Box size (default: 10)')
    parser.add_argument('-b', '--border', type=int, default=4, help='Border size (default: 4)')
    parser.add_argument('--styled', action='store_true', help='Generate styled QR code')
    parser.add_argument('--logo', help='Path to logo image to embed in QR code')
    parser.add_argument('--multiple', action='store_true', help='Generate multiple QR codes from comma-separated data')
    
    args = parser.parse_args()
    
    # Check if qrcode library is installed
    try:
        import qrcode
    except ImportError:
        print("Error: qrcode library not found. Install it with: pip install qrcode[pil]")
        sys.exit(1)
    
    if args.multiple:
        data_list = [item.strip() for item in args.data.split(',')]
        generated_files = generate_multiple_qrs(data_list, size=args.size, border=args.border)
        print(f"Generated {len(generated_files)} QR codes: {', '.join(generated_files)}")
    elif args.logo:
        generate_qr_with_logo(args.data, args.logo, args.output, args.size, args.border)
    elif args.styled:
        generate_styled_qr(args.data, args.output, args.size, args.border)
    else:
        generate_basic_qr(args.data, args.output, args.size, args.border)

if __name__ == "__main__":
    # If no command line arguments, run interactive mode
    if len(sys.argv) == 1:
        print("QR Code Generator - Interactive Mode")
        print("=" * 40)
        
        data = input("Enter data to encode: ")
        output = input("Enter output filename (default: qrcode.png): ").strip() or "qrcode.png"
        
        print("\nChoose QR code style:")
        print("1. Basic (black and white)")
        print("2. Styled (rounded corners, gradient)")
        print("3. With logo (requires logo file)")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "2":
            generate_styled_qr(data, output)
        elif choice == "3":
            logo_path = input("Enter path to logo image: ").strip()
            generate_qr_with_logo(data, logo_path, output)
        else:
            generate_basic_qr(data, output)
    else:
        main()


