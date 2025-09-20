from PIL import Image
from tkinter import Tk, filedialog

def select_two_images():
    root = Tk()
    root.withdraw()
  
    image1_path = filedialog.askopenfilename(
        title="Select First Image", 
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )
    image2_path = filedialog.askopenfilename(
        title="Select Second Image", 
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )

    if not image1_path or not image2_path:
        print("Image selection cancelled.")
        return None, None

    img1 = Image.open(image1_path).convert("RGB")
    img2 = Image.open(image2_path).convert("RGB")


    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.Resampling.LANCZOS)

    return img1, img2



def select_image():
    root = Tk()
    root.withdraw()
  
    image1_path = filedialog.askopenfilename(
        title="Select Image", 
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )

    if not image1_path:
        print("Image selection cancelled.")
        return None

    img1 = Image.open(image1_path).convert("RGB")

    return img1
