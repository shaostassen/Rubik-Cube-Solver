import cv2
import numpy as np

# Define the HSV color ranges for the 6 colors
# Ranges should be broad enough to account for variations in lighting & narrow enough to avoid false positives
color_ranges = {
    'red': ([65, 80, 225], [90, 100, 240]),      # Red hue range (lower)
    'blue': ([190, 115, 70], [210, 135, 100]),  # Blue hue range (narrowed)
    'white': ([210, 230, 235], [235, 245, 245]),     # Higher value (brightness), low saturation
    'orange': ([70, 140, 245], [90, 160, 255]), # Orange hue range
    'green': ([80, 175, 80], [103, 190, 105]),  # Green hue range (narrowed)
    'yellow': ([70, 240, 230], [95, 245, 245])  # Yellow hue range (narrowed)
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
    #hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #cv2.imwrite('hsv_image1.png', hsv_image)
    
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
            sticker_region = image[y_start:y_start+sticker_size, x_start:x_start+sticker_size]
            
            # Detect the color of the sticker
            detected_color = detect_color(sticker_region)
            colors.append(detected_color)
    
    return colors

# Example usage
image_path = 'image/orange.jpeg'
cube_face_colors = extract_rubiks_colors(image_path)
print("Detected colors for the Rubik's Cube face:", cube_face_colors)