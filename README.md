Usage:python3/python main2.py [-h] --image IMAGE [--background BACKGROUND] [--size SIZE] --colors [COLORS [COLORS ...]]
<br>
A utility which can remove specified colors from an image and make that part transparent, resize images, paste one image on other.
<br>
arguments:<br>
  -h, --help  <br>          
show this help message and exit
<br>
  --image IMAGE, -i IMAGE, ***Required Argument***<br>
The image in which color should be made transparent<br>

  --background BACKGROUND, -b BACKGROUND<br>
The image on which first image is being pasted<br>

  --size SIZE, -s SIZE  <br>
Size of resized image in the form of width,height For example- 500,500 <br>

  --colors [COLORS [COLORS ...]], -c [COLORS [COLORS ...]] ***Required Argument***<br>
RGBA codes of colors to be made transparent. R=Red, G=Green, B=Blue, A=Alpha(Enter 225 if not known)
<br><br><br>
Run `pip3 install requirements.txt` (Linux)<br>
Run `pip install -r requirements.txt` (Windows)
