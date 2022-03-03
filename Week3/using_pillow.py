from PIL import Image

im = Image("dog.jpeg")
new_im = im.rotate(90)
new_im.save("dog_rotated.jpeg")