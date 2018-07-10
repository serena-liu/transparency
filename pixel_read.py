from PIL import Image

im = Image.open('ct_blk_gryborder.png') # Can be many different formats.
pix = im.load()
rgb_im = im.convert('RGBA')
# Get the width and hight of the image for iterating over

#take in all the pixel values to read what value it maps to
#compress array based on size of area with the same value.
finalArray = []
overall_pixel_count = 0
pixel_num = im.size[0] * im.size[1]

finalArray.append(im.size[0])
finalArray.append(im.size[1])


for i in range(0, im.size[0]):
    for j in range(0, im.size[1]):
        r,g,b,a = rgb_im.getpixel((i,j))
        average = (r+b+g)/3
        #print(r,g,b,a)
        #print ('\n')

        if (average<=63):
            color = 0
        elif (64<= average <128):
            color = 1
        elif (128<= average <191):
            color = 2
        elif (191<= average <=255):
            color = 3
        
        #Increment based on transparency, higher numbers are more transparent 

        if color ==0:
            if (0<=a<64):
                color= 6
            elif (64<= a < 128):
                color = 5
            elif (128<= a <191):
                color = 4
        elif color ==1:
            if (0<=a<64):
                color= 9
            elif (64<= a < 128):
                color = 8
            elif (128<= a <191):
                color = 7
        elif color == 2:
            if (0<=a<64):
                color= 12
            elif (64<= a < 128):
                color = 11
            elif (128<= a <191):
                color = 10
        elif color == 3:
            if (0<=a<64):
                color= 15
            elif (64<= a < 128):
                color = 14
            elif (128<= a <191):
                color = 13


        #if dis first iteration
        if (i==0 and j==0):
            count = 0 
            last_color = color


        #if the color is the same as the last color, keep going. if not, append the (count, last color) tuple to the array.
        if last_color!=color or count == 255 or (overall_pixel_count + count) >= pixel_num: 
            finalArray.append(count)
            finalArray.append(last_color)
            overall_pixel_count+=count
            count = 1
        elif last_color == color and count < 255:
            count+=1

        last_color = color





finalArray.append(255)
finalArray.append(255)
print(finalArray)
print(pixel_num)
print(overall_pixel_count)
