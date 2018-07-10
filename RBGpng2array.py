#Read in a black and white png image to display 
from PIL import Image

im = Image.open('wpCrossPat-blk-blank.png') # Can be many different formats.
pix = im.load()
rgb_im = im.convert('RGB')
# Get the width and hight of the image for iterating over

#take in all the pixel values to read what value it maps to
#compress array based on size of area with the same value.
finalArray = []

finalArray.append(im.size[0])
finalArray.append(im.size[1])

pixel_num = im.size[0] * im.size[1]
overall_pixel_count = 0


for i in range(0, im.size[0]):
    for j in range(0, im.size[1]):
        r,g,b= rgb_im.getpixel((i,j))
        average = (r+b+g)/3
        #print(r,g,b)

        if (average<=63):
            color = 0
        elif (64<= average <128):
            color = 1
        elif (128<= average <191):
            color = 2
        elif (191<= average <=255):
            color = 3

        #if dis first iteration
        if (i==0 and j==0):
            count = 0
            last_color = color

        if last_color!=color or count == 255 or (overall_pixel_count + count) >= pixel_num: 
            finalArray.append(count)
            finalArray.append(last_color)
            overall_pixel_count += count
            count = 1
        elif last_color == color and count < 255:
            count+=1

        last_color = color




finalArray.append(255)
finalArray.append(255)
print(finalArray)
print(overall_pixel_count)

