import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PIL import Image
from Utils.select_images import select_two_images
from Utils.ouput import display
import numpy as np



def add_images():
   
    img1 , img2 = select_two_images()

    arr1 = np.array(img1, dtype=np.float32)
    arr2 = np.array(img2, dtype=np.float32)
    

    result = np.bitwise_and(arr1.astype(np.uint8), arr2.astype(np.uint8))

    result = Image.fromarray(np.clip(result, 0, 255).astype(np.uint8))

    display(img1,img2,result,"Bit_wise_and")

    

if __name__ == "__main__":
    add_images()
