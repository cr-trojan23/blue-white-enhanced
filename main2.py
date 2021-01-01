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
parser.add_argument("--colors", "-c", action="store", type=str, nargs="*", help="RGB codes of colors to be made transparent")
args = parser.parse_args()


def removeColor():
    img = Image.open("img2.png")
    img = img.convert("RGBA")
    pixdata = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            for i in range(len(args.colors)+1):
                if pixdata[x, y] == args.colors[i]:
                    pixdata[x, y] = (0,0,0,0)
    img.save("img2.png", "PNG")

def resizeImg(img):
    img_re = cv2.imread(img)
    resize = cv2.resize(img_re, args.size)
    cv2.imwrite("img2.png", img_re)

def pasteImg():
    back_img = Image.open(args.background).copy()
    foreg_img = Image.open("img2.png").copy()
    back_img.paste(foreg_img, (0,0), foreg_img)
    back_img.save("final.png", "PNG")

resizeImg(args.image)
removeColor()
pasteImg()