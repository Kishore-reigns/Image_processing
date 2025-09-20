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
    

    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.true_divide(arr1, arr2)
        result[~np.isfinite(result)] = 0 


    result = Image.fromarray(np.clip(result, 0, 255).astype(np.uint8))

    display(img1,img2,result,"division")

    

if __name__ == "__main__":
    add_images()
