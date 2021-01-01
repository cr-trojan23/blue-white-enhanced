An enhanced version of [blue-white](https://www.github.com/cr-trojan23/blue-white)
<br>
usage: main2.py [-h] --image IMAGE [--background BACKGROUND] [--size SIZE] --colors [COLORS [COLORS ...]]

A utility which can remove specified colors from an image and make that part transparent, resize images, paste one image on other.

arguments:
  -h, --help            
show this help message and exit

  --image IMAGE, -i IMAGE, *Required Argument*
The image in which color should be made transparent

  --background BACKGROUND, -b BACKGROUND
The image on which first image is being pasted

  --size SIZE, -s SIZE  
Size of resized image in the form of width,height For example- 500,500

  --colors [COLORS [COLORS ...]], -c [COLORS [COLORS ...]] *Required Argument*
RGBA codes of colors to be made transparent. R=Red, G=Green, B=Blue, A=Alpha(Enter 225 if not known)
<br>
Run pip/pip3 install requirements.txt before running the main2.py
