from PIL import Image
import matplotlib.pyplot as plt
from skimage import io

def display_image_matplotlib(image, img_format, figsize=(4, 3)):
    plt.figure(figsize=figsize)
    plt.imshow(image)
    plt.title(f'Image file format: {img_format}')
    plt.axis('off')  # Turn off axis
    plt.show()


def read_image_matplotlib(file_path):
    image = plt.imread(file_path)
    return image

def convert_image_pil(input_path, output_path, output_format):
    # Read image using PIL
    image_pil = Image.open(input_path)

    # Save image with specified format using PIL
    image_pil.save(output_path, format=output_format)

def convert_image_matplotlib(input_path, output_path, output_format):
    # Read image using Matplotlib
    image_matplotlib = plt.imread(input_path)

    # Save image with specified format using Matplotlib
    plt.imsave(output_path, image_matplotlib, format=output_format)

def convert_image_scikit(input_path, output_path, output_format):
    # Read image using Scikit Image
    image_scikit = io.imread(input_path)

    # Save image with specified format using Scikit Image
    io.imsave(output_path, image_scikit, format=output_format)

def main():
    input_path = input("Enter the file path: ")
    input_format = input('Enter input format of your file: ')
    print(f'Current input file in {input_format} format')
#     of = input('Enter the format you want: ')  
    conversion_format = ['PNG', 'GIF', 'ICO', 'WEBP']
    
    read_img = read_image_matplotlib(file_path=input_path)
    display_image_matplotlib(read_img, img_format='JPG')
    for cf in conversion_format:
        output_path_pil = f"output_pil.{cf.lower()}"
        output_path_matplotlib = f"output_matplotlib.{cf.lower()}"
        output_path_scikit = f"output_scikit.{cf.lower()}"

        # Convert image using PIL
        convert_image_pil(input_path, output_path_pil, cf)
        # Convert image using Matplotlib
        convert_image_matplotlib(input_path, output_path_matplotlib, cf)
        # Convert image using Scikit Image
        convert_image_scikit(input_path, output_path_scikit, cf)
        
        read_img = read_image_matplotlib(file_path=output_path_matplotlib)
        print(f'Done converting in {cf} format')
        display_image_matplotlib(read_img,cf)
        
        
        

if __name__ == "__main__":
    main()
