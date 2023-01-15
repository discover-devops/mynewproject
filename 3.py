from PIL import Image
 
image = input("Enter the image file name: ")
width = input("Enter the new width: ")
height = input("Enter the new height: ")
im = Image.open(image)
width = int(width)
height = int(height)
im_resize = im.resize((width, height), resample=Image.BICUBIC)
im_resize.save("resized_" + image)
