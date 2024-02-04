import cv2
import numpy as np

# Load an existing image
image = cv2.imread('sample.jpg')

# Define parameters for circle arcs
num_arcs = 20
arc_thickness = 2

# Calculate parameters based on image dimensions
height, width, _ = image.shape
arc_radius = min(height, width) // (2 * num_arcs) 

# Generate circle arcs
# for i in range(num_arcs):
i = 1
colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 165, 0),
    (255, 0, 255),
    (0, 255, 255),
    (128, 0, 128)
]

while num_arcs != 34:
    # Calculate center coordinates
    center_x = arc_radius * (i + 1)
    center_y = height - arc_radius * (i + 1) 
    # center_x += 80
    # center_y += 80
    # Define start and end angles
    start_angle = 0
    end_angle = 180
    # Define color based on iteration
    for color in colors:
        print(color)
        # Draw circle arc
        cv2.ellipse(image, (center_x, center_y), (arc_radius, arc_radius), 220, start_angle, end_angle, color, arc_thickness)
    arc_radius += 1
    num_arcs += 1
    i += 1


# Display the image
cv2.imshow('Circle Arcs Over Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
