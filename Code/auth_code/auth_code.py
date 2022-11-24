import tesserocr
from PIL import Image

image1 = Image.open('Code/auth_code/8-2.jpg')
image2 = Image.open('Code/auth_code/8-3.jpg')

#灰度图
def image_shade(image, title):
    image = image.convert('L')
    image.show(title)
    return image

#二值化
def image_convert(image, title):
    image = image.convert('1')
    image.show(title)
    return image

def iamge_shade_with_range(image, title, threshold = 80):
    image = image.convert('L')
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    image.show(title)
    return image
    
if __name__ == '__main__':
    image2.show(title='image2')
    image3 = image_shade(image2, 'image3')
    image4 = image_convert(image2, 'image4')
    image5 = iamge_shade_with_range(image2, 'image5')
    result1 = tesserocr.image_to_text(image1)
    result2 = tesserocr.image_to_text(image2)
    result3 = tesserocr.image_to_text(image3)
    result4 = tesserocr.image_to_text(image4)
    result5 = tesserocr.image_to_text(image5)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)