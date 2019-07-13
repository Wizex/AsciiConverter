# AsciiConverter
I wrote this when i was 16-17 years

How to use:

Function has 3 arguments. First is just image. Second is reduce number (by default 0).
Third is detalization (by default 0), detalization is the difference between pixels in RGB at which we can think that these are different pixels.

Example:

import cv2, VTA


image_path = 'image.png'
image = cv2.imread(image_path)

VTA.convert_image_to_ascii(img, 2, 0)
