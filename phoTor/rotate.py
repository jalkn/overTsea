from PIL import Image

image_path = 'photos/4.png'

def rotate_image_90_degrees(image_path):
    try:
        img = Image.open(image_path)
        rotated_img = img.rotate(90, expand=True)  # Expand the output image to fit the rotated content
        return rotated_img
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None

rotated_image = rotate_image_90_degrees(image_path)

if rotated_image:
    rotated_image.save('photos/4.png')