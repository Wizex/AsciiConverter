# AsciiConverter

How to use:

First you need to install OpenCV

Function has 3 arguments. First is just image. Second is how many times reduce number (by default 0).
Third is detalization (by default 0), detalization is the difference between pixels in RGB at which we can think that these are different pixels.

Example:

```
import cv2
import VTA


image_path = 'image.png'
image = cv2.imread(image_path)

VTA.convert_image_to_ascii(image, 2, 0)
```

After that will be created text file in project folder.
