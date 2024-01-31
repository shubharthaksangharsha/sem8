from PIL import Image
import matplotlib.pyplot as plt
from skimage import io

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
    while True:
        print('Current input file in JPEG format')
        of = input('Enter the format you want: ')  
        
        if 'exit' in of:
            print('thank you for using...')
            break
        input_path = "scenery.png"
        output_path_pil = f"output_pil.{of.lower()}"
        output_path_matplotlib = f"output_matplotlib.{of.lower()}"
        output_path_scikit = f"output_scikit.{of.lower()}"
        

        # Convert image using PIL
        convert_image_pil(input_path, output_path_pil, of)

        # Convert image using Matplotlib
        convert_image_matplotlib(input_path, output_path_matplotlib, of)

        # Convert image using Scikit Image
        convert_image_scikit(input_path, output_path_scikit, of)
        print(f'Done converting in {of} format')

if __name__ == "__main__":
    main()

