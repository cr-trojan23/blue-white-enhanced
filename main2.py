from PIL import Image
import cv2
import argparse


#Command Line Parser
parser = argparse.ArgumentParser(description="A utility to remove specific ")
#Default=logo.png for ACM Research project
parser.add_argument("--image", "-i", type=str, default="logo.png", help="The image in which color should be made transparent", required=True)
#Default=wall.webp for ACM Research project
parser.add_argument("--background", "-b", type=str, default="wall.webp", help="The image on which first image is being pasted", required=False)
parser.add_argument("--size", "-s", type=tuple, help="Size of resized image in the form of (width,height) For example- (500,500)")
parser.add_argument("--colors", "-c", action="store", type=tuple, nargs="*", help="RGB codes of colors to be made transparent")
args = parser.parse_args()


def removeColor(col):
    img = Image.open(col)
    img = img.convert("RGBA")
    pixdata = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            for i in range(len(col)+1):
                if pixdata[x, y] == col[i]:
                    pixdata[x, y] = (0,0,0,0)
    img.save("img2.png", "PNG")

def resizeImg(size):
    img_re = cv2.imread(size)
    resize = cv2.resize(img_re, size)


