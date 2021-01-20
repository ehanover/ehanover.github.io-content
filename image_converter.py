import os
from PIL import Image


dirtarget = "fixedpicturephone"
dircurrent = os.getcwd()
print("running from directory=" + str(dircurrent))
print("processing files in directory=" + str(dirtarget))

# Removes the top notification bar and bottom home bar from phone screenshots
def crop_phone_screenshot(img):
	# Crop the home bar
	homebar = (0, 0, img.size[0], img.size[1] - 168)
	img = img.crop(homebar)

	# Crop the notification bar
	# notificationbar = (0, ???, img.size[0], img.size[1])
	# img = img.crop(notificationbar)

	return img

# Converts png images in a given directory into jpg images with appropriate filenames
i = 0
for f in os.listdir(os.path.join(dircurrent, dirtarget)):
	if ".png" in f:
		img = Image.open(os.path.join(dirtarget, f))
		# img = crop_phone_screenshot(img)

		newname = "imgX" + str(i) + ".jpg"
		# print("saving to new file=" + str(newname))
		img.save(os.path.join(dirtarget, newname))
		i += 1

print("done.")
