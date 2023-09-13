from PIL import Image

# Take list of paths for images
image_path_list = ['IMG_1.jpg', 'IMG_2.jpg', 'IMG_3.jpg', 'IMG_4.jpg', 'IMG_5.jpg']

# Create a list of image objects
image_list = [Image.open(file) for file in image_path_list]

# Save the first image as a GIF file
image_list[0].save(
            'animation2.gif',
            save_all=True,
            append_images=image_list[0:5], # append rest of the images
            duration=300, # in milliseconds
            loop=0)