"""Checks images in a folder, deleting any that are too short or too narrow."""

from PIL import Image
import os

DIRECTORY = "C:/Users/My Dell/Google Drive/"
CRITERIA_WIDTH = 200
CRITERIA_HEIGHT = 200


trashlist = []

for file_name in os.listdir(DIRECTORY):
    try:
        img = Image.open(DIRECTORY + file_name)
        width, height = img.size
        if width < CRITERIA_WIDTH:
            trashlist.append(file_name)
        elif height < CRITERIA_HEIGHT:
            trashlist.append(file_name)
    except:
        pass

for i in trashlist:
    for j in [".jpeg", ".jpg", ".png", ".gif"]:
        if i.endswith(j):
            os.remove(DIRECTORY + i)
            print("Removed ", i)

print(str(len(trashlist)) + " items deleted.")
