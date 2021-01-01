from PIL import Image
import cv2
img_re = cv2.imread("logo.png")
half = cv2.resize(img_re, (500, 400))
cv2.imwrite("img2.png", half)
img = Image.open('img2.png')
img = img.convert("RGBA")
pixdata = img.load()
width, height = img.size
for y in range(height):
    for x in range(width):
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (255, 255, 255, 0)
        if pixdata[x, y] == (15, 27, 112, 255):
            pixdata[x,y] = (0, 0, 0, 0)
img.save("img2.png", "PNG")
img2 = Image.open("img2.png")
img2_cp = img2.copy()
img3 = Image.open("wall.webp")
img3_cp = img3.copy()
img3_cp.paste(img2_cp, (200,60), img2_cp)
img3_cp.save("final.png")