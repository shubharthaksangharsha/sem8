import cv2
import numpy as np
import matplotlib.pyplot as plt

def visualize_frequency_domain(image_path):
    # Function to convert image to frequency domain
    def spatial_to_frequency(image):
        # Convert image to grayscale if it's not already
        if len(image.shape) > 2:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray_image = image

        # Perform FFT
        f_transform = np.fft.fft2(gray_image)
        f_transform_shifted = np.fft.fftshift(f_transform)
        magnitude_spectrum = 20 * np.log(np.abs(f_transform_shifted))

        return magnitude_spectrum

    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Convert image to frequency domain
    frequency_domain = spatial_to_frequency(image)

    # Calculate intensity distribution in spatial domain
    histogram, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

    # Plotting
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Original Image
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    # Frequency Domain Image
    axes[1].imshow(frequency_domain, cmap='gray')
    axes[1].set_title('Frequency Domain')
    axes[1].axis('off')

    # Intensity Distribution
    axes[2].plot(bins[:-1], histogram, color='black')
    axes[2].set_title('Intensity Distribution')
    axes[2].set_xlabel('Pixel Intensity')
    axes[2].set_ylabel('Frequency')

    # Adjust layout
    plt.tight_layout()
    plt.show()

# Call the function with the image path
visualize_frequency_domain('sample.jpg')
