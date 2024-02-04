import cv2
import matplotlib.pyplot as plt

# Load the color image
color_image = cv2.imread('sample.jpg')

# Convert the color image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Generate the negative of the grayscale image
negative_gray_image = 255 - gray_image
while True:
    cv2.imshow('Original Image', color_image)
    if cv2.waitKey(1) == ord('q'):
	    break 
# Display both images using matplotlib
plt.figure(figsize=(10, 5))

# Display grayscale image
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Display negative grayscale image
plt.subplot(1, 2, 2)
plt.imshow(negative_gray_image, cmap='gray')
plt.title('Negative Grayscale Image')
plt.axis('off')

plt.show()

# Save the images if needed
cv2.imwrite('grayscale_image.jpg', gray_image)
cv2.imwrite('negative_gray_image.jpg', negative_gray_image)

