#!/usr/bin/env python3
"""
Create placeholder images for electric car stats when real images cannot be downloaded.
This script creates simple placeholder images with the proper naming scheme.
"""

import json
import os
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def sanitize_filename(filename):
    """Convert filename to filesystem-friendly format"""
    # Replace spaces with hyphens
    filename = filename.replace(' ', '-')
    # Convert to lowercase
    filename = filename.lower()
    # Remove special characters except hyphens and dots
    filename = re.sub(r'[^a-z0-9\-\.]', '', filename)
    return filename


def create_placeholder_image(text, filepath, size=(400, 200)):
    """Create a placeholder image with text"""
    # Create a new image with a light gray background
    img = Image.new('RGB', size, color='#f0f0f0')
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fall back to basic if not available
    try:
        # Try to use a larger font
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        try:
            font = ImageFont.load_default()
        except:
            font = None
    
    # Get text dimensions
    if font:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    else:
        text_width = len(text) * 10
        text_height = 20
    
    # Calculate position to center the text
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Draw the text
    draw.text((x, y), text, fill='#666666', font=font)
    
    # Draw a border
    draw.rectangle([0, 0, size[0]-1, size[1]-1], outline='#cccccc', width=2)
    
    # Save the image
    img.save(filepath)
    print(f"✓ Created placeholder: {filepath}")


def main():
    """Main function to create placeholder images"""
    
    # Get the current directory (project root)
    project_root = Path(__file__).parent
    stats_file = project_root / 'stats.json'
    img_folder = project_root / 'img'
    
    # Check if stats.json exists
    if not stats_file.exists():
        print("Error: stats.json not found")
        return
    
    # Create img folder if it doesn't exist
    img_folder.mkdir(exist_ok=True)
    print(f"Created/verified img folder: {img_folder}")
    
    # Load stats.json
    try:
        with open(stats_file, 'r') as f:
            cars = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing stats.json: {e}")
        return
    
    print(f"Found {len(cars)} cars in stats.json")
    
    # Create placeholder images for each car
    created_count = 0
    skipped_count = 0
    
    for i, car in enumerate(cars):
        make = car.get('make', 'unknown')
        model = car.get('model', 'unknown')
        image_url = car.get('image_url')
        
        if not image_url:
            print(f"⚠ Skipping {make} {model}: No image_url")
            skipped_count += 1
            continue
        
        # Create filename
        filename_base = sanitize_filename(f"{make}-{model}")
        filename = f"{filename_base}.jpg"
        filepath = img_folder / filename
        
        # Skip if file already exists
        if filepath.exists():
            print(f"⚠ Skipping {make} {model}: File already exists at {filepath}")
            skipped_count += 1
            continue
        
        # Create placeholder text
        placeholder_text = f"{make}\n{model}"
        
        print(f"Creating placeholder for {make} {model}")
        
        # Create the placeholder image
        create_placeholder_image(placeholder_text, filepath)
        created_count += 1
    
    print(f"\n✅ Placeholder creation complete!")
    print(f"Created: {created_count} placeholder images")
    print(f"Skipped: {skipped_count} images")
    print(f"Total images in img folder: {len(list(img_folder.glob('*.*')))}")


if __name__ == "__main__":
    main()