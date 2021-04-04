# convert pdf to png todo: hight solution
```py
from wand.image import Image as wImage
from wand.color import Color

from PIL import Image as pImage
img = wImage(
    filename=
    r'C:\Users\14049\WordAndStudy\Projects\python-wand\wand-numpy-explore\test.pdf'
)
imgs = [wImage(image=simg) for simg in list(img.sequence)]

simg = imgs[1]
simg.format = 'png'
simg.background_color = Color('white')
simg.alpha_channel = 'remove'

bsimg = simg.make_blob()  # binary string image

pilImg = pImage.open(bsimg)
```