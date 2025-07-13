# Image Download Instructions

This repository now includes scripts to download and manage car images referenced in `stats.json`.

## Files Created

- **`img/`** - Directory containing all car images with clear, unique names
- **`download_images.py`** - Script to download real images from URLs in `stats.json`
- **`create_placeholders.py`** - Script to create placeholder images (for development/testing)

## Usage

### Download Real Images (Production)

To download actual car images from the URLs in `stats.json`:

```bash
python3 download_images.py
```

This script will:
- Create an `img` folder if it doesn't exist
- Download each image from the `image_url` field in `stats.json`
- Save images with clear names like `tesla-model-3.jpg`, `nissan-leaf.jpg`, etc.
- Skip images that already exist
- Handle download errors gracefully
- Show progress and summary

### Create Placeholder Images (Development/Testing)

To create placeholder images for development when real images aren't available:

```bash
pip install Pillow
python3 create_placeholders.py
```

This creates placeholder images with the same naming scheme as the real images.

## Image Naming Convention

Images are saved with the following naming pattern:
- Format: `{make}-{model}.{extension}`
- Examples: `tesla-model-3.jpg`, `hyundai-kona-electric.jpg`
- Names are lowercase and filesystem-friendly (spaces become hyphens)

## Current Images

The following images are now available in the `img/` folder:

1. `tesla-model-3.jpg` - Tesla Model 3
2. `tesla-model-y.jpg` - Tesla Model Y  
3. `nissan-leaf.jpg` - Nissan Leaf
4. `hyundai-kona-electric.jpg` - Hyundai Kona Electric
5. `volkswagen-id.4.jpg` - Volkswagen ID.4
6. `bmw-ix3.jpg` - BMW iX3
7. `audi-e-tron.jpg` - Audi e-tron
8. `mercedes-eqs.jpg` - Mercedes EQS
9. `ford-mustang-mach-e.jpg` - Ford Mustang Mach-E
10. `lucid-air.jpg` - Lucid Air
11. `rivian-r1t.jpg` - Rivian R1T
12. `polestar-2.jpg` - Polestar 2
13. `genesis-gv60.jpg` - Genesis GV60
14. `kia-ev6.jpg` - Kia EV6
15. `byd-tang.jpg` - BYD Tang
16. `skoda-enyaq.jpg` - Skoda Enyaq

## Dependencies

- **For downloading real images**: `requests` (built-in Python library)
- **For creating placeholders**: `Pillow` (install with `pip install Pillow`)

## Error Handling

The download script includes robust error handling:
- Network timeouts and connection errors
- Invalid URLs or missing images
- File system permission issues
- Progress reporting and detailed logging

## Integration

The images can be used in the web application by updating the `index.html` to reference local images instead of external URLs, providing faster loading and better reliability.