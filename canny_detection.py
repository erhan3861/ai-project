import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("edge.jpg", 0) # 0 paramtresi gri renge çevirir
plt.figure()

edges = cv2.Canny(image=img, threshold1=0, threshold2=255)

plt.imshow(edges, cmap="gray")
plt.title("edges")
plt.axis("off")
plt.show()

median_val = np.median(img)
low = int(max(0, (1-0.33) * median_val))
high = int(min(255, (1+0.33) * median_val))

edges2 = cv2.Canny(image=img, threshold1=low, threshold2=high)

plt.imshow(edges2, cmap="gray")
plt.title("edges 2")
plt.axis("off")
plt.show()

# blur
blurred_img = cv2.blur(img, ksize=(5,5))
plt.figure()
plt.imshow(blurred_img, cmap="gray")
plt.title("blurred_img")
plt.axis("off")
plt.show()

median_val = np.median(blurred_img)
low = int(max(0, (1-0.33) * median_val))
high = int(min(255, (1+0.33) * median_val))

edges_blur = cv2.Canny(image=blurred_img, threshold1=low, threshold2=high)

plt.figure()
plt.imshow(edges_blur, cmap="gray")
plt.title("edges_blur")
plt.axis("off")
plt.show()