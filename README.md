# Electric Car Stats

A responsive web application that displays electric car statistics in an attractive card-based layout.

## Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Car Statistics**: Displays range, price, trunk space, and horsepower for each vehicle
- **Image Support**: Supports displaying car images from URLs
- **Graceful Fallbacks**: Shows placeholder when images fail to load or are not provided
- **Modern UI**: Clean, card-based design with hover effects

## Image URL Support

The application now supports displaying car images from URLs. To add an image to a car entry:

1. Add an `image_url` field to the car object in `stats.json`
2. The image will be displayed at the top of each car card
3. Images are automatically resized to 400x200px with proper aspect ratio handling
4. If an image URL fails to load, a "No Image Available" placeholder is shown

### Example car entry with image:

```json
{
  "make": "Tesla",
  "model": "Model 3",
  "year": 2024,
  "range_km": 430,
  "price_usd": 40000,
  "trunk_space_liters": 425,
  "horse_power": 283,
  "image_url": "https://example.com/tesla-model-3.jpg"
}
```

### Example car entry without image:

```json
{
  "make": "Tesla",
  "model": "Model 3",
  "year": 2024,
  "range_km": 430,
  "price_usd": 40000,
  "trunk_space_liters": 425,
  "horse_power": 283
}
```

## Usage

1. Clone the repository
2. Serve the files using a local web server (e.g., `python3 -m http.server 8000`)
3. Open `http://localhost:8000` in your browser
4. Add or modify car entries in `stats.json` to update the displayed data

## Technical Details

- Built with vanilla HTML, CSS, and JavaScript
- No external dependencies
- Responsive grid layout using CSS Grid
- Error handling for failed image loads
- Semantic HTML structure for accessibility

## Data Structure

Each car entry in `stats.json` supports the following fields:

- `make` (required): Car manufacturer
- `model` (required): Car model name
- `year` (required): Model year
- `range_km` (required): Range in kilometers
- `price_usd` (required): Price in USD
- `trunk_space_liters` (required): Trunk space in liters
- `horse_power` (required): Horsepower
- `image_url` (optional): URL to car image

## Browser Support

- Modern browsers with CSS Grid support
- Chrome, Firefox, Safari, Edge
- Mobile browsers on iOS and Android