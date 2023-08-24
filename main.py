import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.img_tiles as cimgt
import random

print("Loading JSON file...")
# Load the JSON file
with open('lighthouses.json') as f:
    data = json.load(f)

print("Extracting coordinates...")
# Extract the coordinates of each lighthouse
lighthouses = [feature['geometry']['coordinates'] for feature in data['features']]

print("Creating map...")
# Create a Stamen terrain background instance.
stamen_terrain = cimgt.Stamen('terrain-background')

fig = plt.figure()

# Create a GeoAxes in the tile's projection.
ax = plt.axes(projection=stamen_terrain.crs)

# Limit the extent of the map to a small longitude/latitude range.
ax.set_extent([-25, 45, 34, 72], crs=ccrs.Geodetic())

print("Adding terrain...")
# Add the Stamen data at zoom level 8.
ax.add_image(stamen_terrain, 8)

print("Plotting lighthouses...")
# Plot each lighthouse on the map with leaner points
points = [plt.plot(*coords, 'ro', markersize=2, transform=ccrs.Geodetic())[0] for coords in lighthouses]

print("Creating animation...")
# Create a function to update the visibility of each lighthouse
def update(num):
    for point in points:
        point.set_visible(random.choice([True, False]))

ani = animation.FuncAnimation(fig, update, frames=range(100), interval=100)

print("Saving animation...")
# Save the animation as an mp4 file
ani.save('lighthouses.mp4', writer='ffmpeg')

print("Animation saved. Displaying plot...")
plt.show()