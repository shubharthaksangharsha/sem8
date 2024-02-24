import cv2
import matplotlib.pyplot as plt

# Load the color image
image_path = "sample3.jpg"
color_image = cv2.imread(image_path)

# Convert the color image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Generate the negative of the grayscale image
negative_gray_image = 255 - gray_image

# Display all three images using matplotlib
plt.figure(figsize=(15, 5))

# Display original color image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
plt.title('Original Color Image')
plt.axis('off')

# Display grayscale image
plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Display negative grayscale image
plt.subplot(1, 3, 3)
plt.imshow(negative_gray_image, cmap='gray')
plt.title('Negative Grayscale Image')
plt.axis('off')

plt.show()

# Save the images if needed
cv2.imwrite(f'{image_path}_grayscale_image.jpg', gray_image)
cv2.imwrite(f'{image_path}_negative_gray_image.jpg', negative_gray_image)
