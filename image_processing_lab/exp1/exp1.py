'''
Experiment1: WAP to Read, Save and display image using the following libaries:- 
1. Matplotlib
2. Scikit-Image
3. PIL
'''

#By Shubharthak, 20BCS6872
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io

def read_image_pil(file_path):
    image = Image.open(file_path)
    return image

def save_image_pil(image, output_path):
    image.save(output_path)

def display_image_pil(image):
    image.show()

def read_image_matplotlib(file_path):
    image = plt.imread(file_path)
    return image

def save_image_matplotlib(image, output_path):
    plt.imsave(output_path, image)

def display_image_matplotlib(image):
    plt.imshow(image)
    plt.show()

def read_image_scikit(file_path):
    image = io.imread(file_path)
    return image

def save_image_scikit(image, output_path):
    io.imsave(output_path, image)

def display_image_scikit(image):
    io.imshow(image)
    io.show()

def main():
    file_path = "pic.jpeg"
    of = input('Enter the format you want: ')
    output_path_pil = f"output_pil.{of}"
    output_path_matplotlib = f"output_matplotlib.{of}"
    output_path_scikit = f"output_scikit.{of}"

    # Reading and displaying images using PIL
    image_pil = read_image_pil(file_path)
    display_image_pil(image_pil)

    # Saving the PIL image
    save_image_pil(image_pil, output_path_pil)

    # Reading and displaying images using Matplotlib
    image_matplotlib = read_image_matplotlib(file_path)
    display_image_matplotlib(image_matplotlib)

    # Saving the Matplotlib image
    save_image_matplotlib(image_matplotlib, output_path_matplotlib)

    # Reading and displaying images using Scikit Image
    image_scikit = read_image_scikit(file_path)
    display_image_scikit(image_scikit)

    # Saving the Scikit Image
    save_image_scikit(image_scikit, output_path_scikit)

if __name__ == "__main__":
    main()

