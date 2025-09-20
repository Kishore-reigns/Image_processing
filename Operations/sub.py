import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PIL import ImageChops
from Utils.select_images import select_two_images
from Utils.ouput import display



def add_images():
   
    img1 , img2 = select_two_images()
    result = ImageChops.difference(img1, img2)

    display(img1,img2,result,"subtract")

    

if __name__ == "__main__":
    add_images()
