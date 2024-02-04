import cv2
import matplotlib.pyplot as plt

def show_menu():
    print("Select Color Space Conversion:")
    print("1. BGR to Grayscale")
    print("2. BGR to HSV")
    print("3. BGR to LAB")
    print("4. BGR to XYZ")
    print("5. BGR to YCrCb")
    print("6. BGR to HLS")
    print("7. BGR to Luv")
    print("8. BGR to YUV")
    print("9. BGR to Lab")
    print("10. BGR to Luv")
    print("11. BGR to RGB")
    print("12. ALL")
    print("13. Exit")
    choice = int(input("Enter your choice (1-13): "))
    return choice

def convert_color_space(image, choice):
    if choice == 1:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), "GRAYSCALE"
    elif choice == 2:
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV), "HSV"
    elif choice == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2LAB), "LAB"
    elif choice == 4:
        return cv2.cvtColor(image, cv2.COLOR_BGR2XYZ), "XYZ"
    elif choice == 5:
        return cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb), "YCrCb"
    elif choice == 6:
        return cv2.cvtColor(image, cv2.COLOR_BGR2HLS), "HLS"
    elif choice == 7:
        return cv2.cvtColor(image, cv2.COLOR_BGR2Luv), "Luv"
    elif choice == 8:
        return cv2.cvtColor(image, cv2.COLOR_BGR2YUV), "YUV"
    elif choice == 9:
        return cv2.cvtColor(image, cv2.COLOR_BGR2Lab), "Lab"
    elif choice == 10:
        return cv2.cvtColor(image, cv2.COLOR_BGR2Luv), "Luv"
    elif choice == 11:
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "RGB"
    else:
        return None, None

def main():
    while True:
        # Read the image
        image = cv2.imread('sample.jpg')

        # Show menu and get user choice
        choice = show_menu()

        if choice == 13:
            print("Exiting program...")
            break
        elif choice == 12:  # ALL option
            num_rows = 3  # Number of rows in the subplot grid
            num_cols = 4  # Number of columns in the subplot grid
            plt.figure(figsize=(15, 10))
            for i in range(1, 12):
                converted_image, name = convert_color_space(image, i)
                if converted_image is not None:
                    plt.subplot(num_rows, num_cols, i)
                    plt.imshow(converted_image, cmap='gray' if name == 'GRAYSCALE' else None)
                    plt.title(name)
                    plt.axis('off')
            plt.tight_layout()
            plt.show()
            continue

        # Perform color space conversion based on user choice
        converted_image, name = convert_color_space(image, choice)
        if converted_image is None:
            print("Invalid choice. Please select a valid option (1-13).")
            continue

        # Display the original and converted images (optional)
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title("Original Image")
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(converted_image, cmap='gray' if name == 'GRAYSCALE' else None)
        plt.title(f'Converted Image ({name})')
        plt.axis('off')
        plt.show()

        

if __name__ == "__main__":
    main()
