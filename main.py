import requests
from io import BytesIO
from PIL import Image
from dalle_mini.model import CustomDALLE
from dalle_mini.utils import download_image, generate_images


# The generate_image_dalle function takes a prompt as input and generates a new image based on the given prompt. It uses the DALL-E mini model.

# Here's a description of the steps involved:

# Load the DALL-E mini model using the CustomDALLE class.
# Generate images using the DALL-E mini model by passing the prompt to the generate_images function.
# Choose the first image from the generated images.
# The function returns the generated image as a PIL Image object. You can save the generated image to a file using the save() method, as shown in the example usage.
def generate_image_dalle(prompt):
    # Load the DALL-E mini model
    dalle = CustomDALLE()

    # Generate images with DALL-E mini
    generated_images = generate_images(prompt, model=dalle)

    # Choose the first image from the generated images
    generated_image = generated_images[0]

    return generated_image


def main():
  # Example usage
  prompt = "sunset with mountains in the background"
  generated_image = generate_image_dalle(prompt)
  generated_image.save("generated_image.jpg")

if __name__ == "__main__":
    main()

