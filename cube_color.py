import cv2
import numpy as np

# Define the HSV color ranges for the 6 colors
# Ranges should be broad enough to account for variations in lighting & narrow enough to avoid false positives
color_ranges = {
    'white': ([0, 0, 200], [180, 30, 255]),     # Higher value (brightness), low saturation
    'red': ([0, 150, 50], [10, 255, 255]),      # Red hue range (lower)
    'orange': ([10, 100, 100], [25, 255, 255]), # Orange hue range
    'blue': ([90, 100, 100], [130, 255, 255]),  # Blue hue range (narrowed)
    'green': ([40, 100, 100], [80, 255, 255]),  # Green hue range (narrowed)
    'yellow': ([25, 150, 150], [35, 255, 255])  # Yellow hue range (narrowed)
}

# Helper function to detect color of a given region
def detect_color(hsv_region):
    for color_name, (lower, upper) in color_ranges.items():
        lower_bound = np.array(lower, dtype="uint8")
        upper_bound = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv_region, lower_bound, upper_bound)
        if np.sum(mask) > 0:  # If any pixels match the color
            return color_name
    return 'unknown'

# Function to process the image and extract the colors of the 9 stickers
def extract_rubiks_colors(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Resize the image to make processing easier
    image = cv2.resize(image, (300, 300))  # Assuming a square image of the cube face
    
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define grid dimensions for the 3x3 face
    grid_size = 3
    sticker_size = 100  # Size of each square in the 3x3 grid

    colors = []

    # Loop through the 3x3 grid to extract colors
    for row in range(grid_size):
        for col in range(grid_size):
            # Extract the region of interest (a single sticker)
            y_start = row * sticker_size
            x_start = col * sticker_size
            sticker_region = hsv_image[y_start:y_start+sticker_size, x_start:x_start+sticker_size]
            
            # Detect the color of the sticker
            detected_color = detect_color(sticker_region)
            colors.append(detected_color)
    
    return colors

# Example usage
image_path = 'image/white.jpeg'
cube_face_colors = extract_rubiks_colors(image_path)
print("Detected colors for the Rubik's Cube face:", cube_face_colors)