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

VTA.convert_image_to_ascii(image, 6, 0)
```

After that will be created text file in project folder.


Image:

![Image](https://img.favpng.com/6/25/22/squidward-tentacles-patrick-star-plankton-and-karen-morty-smith-character-png-favpng-qLV8Vuxq2pgsYWyMFqsdCn78W.jpg)


Image converted to ASCII:
'''
\\`\`\\`\`\\`\`\\`\`\]_]`@&"3X\Z^\`\\`\`\\`\`\\`\`\
\\`\`\\`]`\\`\`\[`!"!JJJJJJJJJJJJ2!!Z`\`\\`\`\\`]`\
``\`\``\`\``\`4!JJJJ%!JJIJJJ!JJJJJJJJJ!]``\`\``\`\`
\\`\`\\`\`\\!JIJJJJJJJJJHJJJJJJJIJJJJ!JJ!#`\`\\`\`\
``\`\``\`[!JJ!JJJJJJJJJJ!JJJJJJJ!JJJJJJJJJ"`\``\`\`
\\`\`\\_-DJJJJJJ!"JJJJJJJJJJJIJIIIJJJJJJJJJJ!\\`\`\
]\`\`]\"JJJJJJJJJJJJJJJI<!!!;JJJJJJ:!!!JKJJJJ!\`\`\
``\`\^!JI!JJJJJJJJJKJ!%JJJJJJJJJJJJJJJJJI!!IJJ!\`\`
\\`]^"JJJJJJJJJJJI!IJJJJJJJIH!!!!!!!!!JIJJJJJJJ"\`\
``\`!JJJJJJJJJJJJJJJJJII!!JJJJJJJJJJJJJJ!!JJJJJJ!\`
\\_!JJJJJJJJJJJJJJJJJ!!JJJJJJJJJJJJJJJJJJJJ!!IJJI-\
\\`JJJJJJJJJJJJJJJK!JJJJJJJJJJJJJJJJJJJJJJJJJ"!JJ'\
``!JJJJJJJJJJJJJJ!JJJJJJJJJJJJIIJG:<IJJJJJJJJJJ(JJ"
\]JJJJJJJJJJJJJJJJJJJJJJII>!!EJJJJJJJJJJ!!!IJJJJJJ!
`!JJJJJJJJJJJJJJJJJJJJJ!!JJJJJJJJJJJJJJJJJJI!IJJJJJ
]GJJJJJJJJJJJJJJJJJJI!JJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
\JJJJJJJJJJJJJJJJJJJJJJJJJJHIJJJJJJJIJIIJJJJJJJJJJJ
^JJJJJJJJJJJJJJJJJJJJJJJJI!DDDD"HJI"DDDD!JJJJJJJJJJ
)JJJJJJJJJJJJJJJJJJJJJJJJ"DDDDDDCJ"DDDDDD!JJJJJJJJJ
4JJJJJJJJJIJJJJJJJJJJJJJ"DDDDDDDD!DDDDDDDDIJJJJJJJJ
\JJJJJJJJJJJJJJJJJJJJJJKDDDDDDDDDDCDDDDDDD!JJJJJJJI
]JJJJJJJJJJJJJJJJJJJJJJ2DDDDDDDDDD!DDDDDDDDJJJJJJJI
`!JJJJJJJJJJJJJJJJJJJJJ!DEE!!!!!!!-!!+)!!-EJJJJJJJ!
\!JJJJJJJJJJJJJJJJJJJJJ!QQQQQQ..QQQQQQ0.QQQJJJJJJJH
``7JJJJJJJJJJJJJJJJJJJIQQQQQQQ..QQPQQQ0.QQQJJJJJJ!`
\\*JJJJJJJJJJJJJJJJJJJIQQQQQQQ..QQQQQQ0.QQQJJJJJI`\
\\`!JJJJJJJJJJJJJJJJJJIQQQQQQQ..QQQQQQ0.QQQJJJJJ'`\
``\`!JJJJJJJJJJJJJJJJJJQQQQQQQ..QQQQQQ0.QQQJJJI"`\`
\\`\`!HJJJJJJJJJJJJJJJJQQQQQQQ-.QQQQQQ0.QQQJK<\`\`\
``\`\``!IJJJJJJJJJJIJJJQQQQQQQ1.QQRQQQ1.QQQI"``\`\`
\\`\`\\_:!IJJJJJJJJJJJJ!QQQQQQQQQQPQQQQQQQ8\`\\`\`\
\[`\`\\`\`\!!IIJIJJ!JJJ'QQQQQQQQQQH!FRQQQQ!\`\\`\`\
`_\`\``\`\``\`\`1!!!JJJJQQQQQQQQQQ!JJH!QQQ\`\``\`\`
\\`\`\\`\`\\`\`\\`\!JJJJ"QQQQQQQQPJJJJJ.OP`\`\\`\`\
``\`\``\`\``\`\``\`!JJJJIQQQQQQQQ"JJJJJJI!\`\``\`\`
\\`\`\\`\`\\`\`\\`\!JJJJJ"QQQQQQQIJJJJJJJH!\`\\`\`\
\\`\`\\`\`\\`\`\\`\!JJJJJJ!QQQQSJJ!JJJJJJJH\`\\`\`\
``\`\``\`\``\`\``\`!JJJJJJJ#0L"JJJ!JJJJJJJJ!\``\`\`
\\`\`\\`\`\\`\`\\`\!JJJJJJJJJJJJJJ!JJJJJJJJJ!\\`\`\
``\`\``\`\``\`\``\`#JJJJJJJJJJJJJJ!JJJJJJJJJ&``\`\`
\\`\`]\`\`\\`\`\\`\'JJJJJJJJJJJJJJ!JJJJJJJJJJ\\`\`\
\\`\`\\`\`\\`\`\\`"!JJJJJJJJJJJJJJJJJJJJJJJJJ!\`\`\
``\`\``\`\``\`\`!CJJJJJJIJJJJJIIJ#JJJJJJJJJJJ!`\`\`
\\`\`\\`\`\\`]X*JJJJJJJJIJ!!IJJJJJJJJJJJJJJJJJ\`\`\
``\`\``\`\``Z!JJJJJJJI"!JJJJJJJJJ!JJJJJJJJJJJJ`\`\`
\]`\`\\`\`\\]JIJJJJG&JJJJJJJJJJII!JJJJJJJJJJJI\`\`\
]\`\`\\`\`\[!JJJ"!JJJJJJJJJJ!"\\`!JJJJJJJJJJJI\`\`\
``\`\``\`\``!JIJ!JJJJJJIJ!3JJ+``\!JJJJJJJJJJJJ`\`\`
\\`\`\\`\`\\!JIIJJJJJH!!JJIJJ`\\`!JJJJJJJJJJJI\`\`\
``\`\``\`\``\!JJJJK!!`\`JJJJI\``\!JJJJJJJJJJJ!`\`\`
\]`\`\\`\`\\`\"!!!\`\\`\JJJJ!`\\`!JJJJJJJJJJJ!\`\`\
\\`\`\\`\`\\`\`\\`\`\[`\JJIJ\`\\`\JJJJJJJJJJJ\\`\`\
``\`\`_\`\``\`\``\`\``\`JJJJ`\``\`!JJJJJJJJJ!``\`\`
\\`\`\\`\`\\`\`\\`\`\\`\JJJI\`\\`\`1JJJJJJJK`\\`\`\
``\`\``\`\_`\`\``\`\``\`JJJ=`]``\`\`!IJJJJH!\``\`\`
\\`\`\\`\`\\`\`\\`\`\\`\FJJ!\`\\`\`\\`!!E!`\`\]`\`\
\\`\`\\`\`\\`\`][`\`\[`\:JJ!\`]\`\`\\`]`\\`\`\\`\`\
``\`\``\`\``\`\``\`\`_\`+JI"`\``\`\``\`\``\`\``\`\`
\\`\`\\`\`\\`\`\\`\`\\`\!JJZ\`\\`\`\\`\`\\`\`\\`\`\
``\`\``\`\``\`\`_\`\``\`!JJ\`\``\`\``\`\``\`]``\`\`
\\`\`\\`\`\\`\`\\`\`\\`[!JJ`\`\\`\`\\`\`\\`\`\\`\`\
\\`\`\\`\`\\`]`\\`\`]\`!!JJ`\`]\`\`\\`\`\\`\`\\`]`\
``\`\``\`\``\`\``\`\``[3!JJ$#\``\`\``\`\``\`\``\`\`
\\`\`\\`\`\\`\`\\`\`\\^43IJ!3`\\`\`\\`\`\\`\`\\`\`\
``\`\``\`\``\`\``\`\`_!443K!!\``\`\``\`\``\`\``\`\`
\\`\`\\`\_\\`\`\\`\`\\!6431!*$]\`\`\]`\`\\`\`\\`\`\
\\`\`\\`\`\\`\`\\`\`\[33334!!%\\`\`]\`]`\\`\`\\`\`\
``\`\``\`\``\`\``\`\`,34!!3"41``\`\``\`\``\`\``\`\`
\]`\`\\`\`\\`\`\\`\`\"33443433\]`\`\\`\`\\`\`\\`\`\
``\`\``\`\``\`\``\`\`333333333``\`\``\`\``\`\``\`\`
\\`\`\]`\`\\_\`\\`\`\433333334!\`\`\\`\`\\`\`]\`\`\
]\`\`\\`\`\\`\`\\`\`U333333334$\`\`\\`\`\\`\`]\`\`\
'''
