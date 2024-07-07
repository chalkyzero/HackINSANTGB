import cv2
import numpy as np
from sklearn.cluster import KMeans

# Function to load and decode the image
def load_image(image_path):
    # Read the image from the specified file path
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unable to read the image.")
    return image

# Function to calculate the percentage of greenery
def calculate_greenery_percentage(image):
    # Convert the image from BGR (OpenCV default) to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range for the green color in HSV space
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Create a mask for green areas in the image
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Calculate the percentage of green pixels
    green_pixels = np.sum(mask > 0)
    total_pixels = mask.size
    green_percentage = (green_pixels / total_pixels) * 100

    return green_percentage

# Main function
def main():
    # Path to the image file
    image_path = 'google_earth_image.jpg'

    # Load and decode the image
    image = load_image(image_path)

    # Calculate the percentage of greenery in the image
    green_percentage = calculate_greenery_percentage(image)

    # Print the result
    print(f"The percentage of greenery in the image is: {green_percentage:.2f}%")

if __name__ == "__main__":
    main()
