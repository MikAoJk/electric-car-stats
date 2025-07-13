#!/usr/bin/env python3
"""
Script to download all images referenced by image_url fields in stats.json
and save them to an img folder at the project root.
"""

import json
import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote
import time


def sanitize_filename(filename):
    """Convert filename to filesystem-friendly format"""
    # Replace spaces with hyphens
    filename = filename.replace(' ', '-')
    # Convert to lowercase
    filename = filename.lower()
    # Remove special characters except hyphens and dots
    filename = re.sub(r'[^a-z0-9\-\.]', '', filename)
    return filename


def get_file_extension(url):
    """Extract file extension from URL"""
    parsed = urlparse(url)
    path = unquote(parsed.path)
    ext = os.path.splitext(path)[1]
    
    # Default to .jpg if no extension found
    if not ext:
        ext = '.jpg'
    
    return ext


def download_image(url, filepath):
    """Download image from URL and save to filepath"""
    try:
        # Add headers to mimic a real browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Downloaded: {filepath}")
        return True
        
    except requests.RequestException as e:
        print(f"✗ Failed to download {url}: {e}")
        return False


def main():
    """Main function to download all images from stats.json"""
    
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
    
    # Download images for each car
    downloaded_count = 0
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
        extension = get_file_extension(image_url)
        filename = f"{filename_base}{extension}"
        filepath = img_folder / filename
        
        # Skip if file already exists
        if filepath.exists():
            print(f"⚠ Skipping {make} {model}: File already exists at {filepath}")
            skipped_count += 1
            continue
        
        print(f"Downloading {make} {model} from {image_url}")
        
        # Download the image
        success = download_image(image_url, filepath)
        
        if success:
            downloaded_count += 1
        
        # Add a small delay to be respectful to servers
        time.sleep(0.5)
    
    print(f"\n✅ Download complete!")
    print(f"Downloaded: {downloaded_count} images")
    print(f"Skipped: {skipped_count} images")
    print(f"Total images in img folder: {len(list(img_folder.glob('*.*')))}")


if __name__ == "__main__":
    main()