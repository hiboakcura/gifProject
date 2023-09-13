from PIL import Image

# Take list of paths for images
image_path_list = ['img_3.png', 'img_4.png', 'img_5.png', 'img_6.png', 'img_7.png']

# Create a list of image objects
image_list = [Image.open(file) for file in image_path_list]

# Save the first image as a GIF file
image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[0:], # append rest of the images
            duration=400, # in milliseconds
            loop=0)