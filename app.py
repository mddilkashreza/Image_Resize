# install pillow if you havent
# import pillow
# open up the image we want to resize using python
# print the current size of that image
# specify the size we wanna change it to 
# save the new resized image

from PIL import Image


def resized_image(size1, size2):
    image = Image.open('D:\python\webscraper\dd.jpeg')
    print(f"Current size : {image.size}")

    resize_image = image.resize((size1, size2))

    resize_image.save('spiderman-500'+str(size1)+'.jpeg')

size1 = int(input('Enter width:'))
size2 = int(input('Enter length'))
resized_image(size1,size2)