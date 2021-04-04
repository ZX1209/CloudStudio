Imageio is a Python library that provides an easy interface to read and
write a wide range of image data, including animated images, volumetric
data, and scientific formats. It is cross-platform, runs on Python 2.7
and 3.4+, and is easy to install.


merge pngs to gif
```py
import imageio
import os

images = []
filenames = sorted((fn for fn in os.listdir(
    'splitPngs/') if fn.endswith('.png')))

for filename in filenames:
    images.append(imageio.imread('splitPngs/'+filename))

imageio.mimsave('mergeGif2.gif', images)

```