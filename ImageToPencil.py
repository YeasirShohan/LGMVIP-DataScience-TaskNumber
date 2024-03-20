import cv2
import numpy as np

def pencil_sketch(image_path):
    # Read the image in grayscale
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Invert the grayscale image
    inverted_gray_image = cv2.bitwise_not(gray_image)

    # Apply Gaussian blur to the inverted grayscale image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    # Create the pencil sketch by taking the absolute difference between the grayscale image and the inverted blurred image
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=168.0)

    # Increase the contrast of the pencil sketch image
    pencil_sketch_image = cv2.multiply(pencil_sketch_image, 1.5)

    # Show the original image and the pencil sketch
    cv2.imshow('Original Image', gray_image)
    cv2.imshow('Pencil Sketch', pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function with the image path
pencil_sketch('G:\My photo\Snapseed.jpg')
