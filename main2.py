from PIL import Image
import cv2
import argparse
import os


#Command Line Parser
parser = argparse.ArgumentParser(description="A utility which can remove specified colors from an image and make that part transparent, resize images, paste one image on other.")
#Default=logo.png for ACM Research project
parser.add_argument("--image", "-i", type=str, default="logo.png", help="The image in which color should be made transparent", required=True)
#Default=wall.webp for ACM Research project
parser.add_argument("--background", "-b", type=str, default="wall.webp", help="The image on which first image is being pasted", required=False)
parser.add_argument("--size", "-s", action="store", type=str, help="Size of resized image in the form of width,height For example- 500,500", required=False)
parser.add_argument("--colors", "-c", action="store", type=str, nargs="*", help="RGBA codes of colors to be made transparent. R=Red, G=Green, B=Blue, A=Alpha(Enter 225 if not known)", required=True)
args = parser.parse_args()


def removeColor(colors):
    img = Image.open("img2.png")
    img = img.convert("RGBA")
    pixdata = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            for i in range(len(colors)):
                color = tuple(map(int, colors[i].split(",")))
                if pixdata[x, y] == color:
                    pixdata[x, y] = (0,0,0,0)
    img.save("img2.png", "PNG")

def resizeImg(img):
    size = tuple(map(int, args.size.split(",")))
    img_re = cv2.imread(img)
    resize = cv2.resize(img_re, size)
    cv2.imwrite("img2.png", resize)

def pasteImg():
    back_img = Image.open(args.background).copy()
    foreg_img = Image.open("img2.png").copy()
    back_img.paste(foreg_img, (0,0), foreg_img)
    back_img.save("final.png", "PNG")
    os.remove("img2.png")

resizeImg(args.image)
removeColor(args.colors)
pasteImg()