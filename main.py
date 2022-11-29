import sys
import os
import cv2 as cv

if len(sys.argv) == 1:
    path = "./Images"
else:
    path = sys.argv[1]

images = []

for file in os.listdir(path):
    fileName, ext = os.path.splitext(file)
    if not ext in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        continue

    images.append(os.path.join(path, file))

img = cv.imread(images[0])
width, height, channels = img.shape
size = (width, height)

writer = cv.VideoWriter("vid.mp4", cv.VideoWriter_fourcc(*"DIVX"), 0.8, size)
for img in images:
    writer.write(cv.imread(img))
