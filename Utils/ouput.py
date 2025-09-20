import matplotlib.pyplot as plt

def display(img1,img2,result,operation):
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.title("Image 1")
    plt.imshow(img1)
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Image 2")
    plt.imshow(img2)
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("Operation : " + operation )
    plt.imshow(result)
    plt.axis("off")

    plt.tight_layout()
    plt.show()