import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PIL import Image
from Utils.select_images import select_image
from Utils.ouput import display_one
import numpy as np



def add_images():
   
    img1 = select_image()

    arr1 = np.array(img1, dtype=np.float32)
  
    

    result = np.bitwise_not(arr1.astype(np.uint8))

    result = Image.fromarray(np.clip(result, 0, 255).astype(np.uint8))

    display_one(img1,result,"Bit_wise_not")

    

if __name__ == "__main__":
    add_images()
