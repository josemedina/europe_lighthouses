# European Lighthouses Map Animation

This project generates an animated map of lighthouses along the European coast. The lighthouses are represented as points on the map, which flash randomly to simulate the operation of a lighthouse.

## Requirements

- Python 3.9 or higher
- Cartopy
- Matplotlib
- ffmpeg

## Installation

1.Clone this repository:
    
    https://github.com/josemedina/europe_lighthouses.git

2. Install the required Python packages:
    
    pip install -r requirements.txt
    
## Usage

Run the script with:
    
    python main.py

This will generate an mp4 file named 'lighthouses.mp4' in the same directory.

## Data

The data for the lighthouses is stored in a JSON file named 'lighthouses.json'. Each lighthouse is represented as a feature with a point geometry and properties including the name, country, and coordinates.

## Map

The map is generated using the Cartopy library, which provides cartographic tools for Python. The map includes a representation of the European coast, country borders, and terrain. The lighthouses are plotted on the map using their coordinates.

## Animation

The animation is created using the Matplotlib library. Each lighthouse flashes randomly by alternating its visibility in each frame.

*Based on the high level rendering of the terrain the generation of the video might takes a few minutes running depending on your machine specs. 5-10 minutes is the average. 

