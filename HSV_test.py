import cv2

# Function to inspect the HSV value of a pixel
def inspect_hsv(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            hsv_value = hsv_image[y, x]  # Get HSV value at (x, y)
            print(f"HSV at ({x}, {y}) is: {hsv_value}")
    
    cv2.imshow('Image', image)
    cv2.setMouseCallback('Image', mouse_callback)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'image/white.jpeg'
inspect_hsv(image_path)