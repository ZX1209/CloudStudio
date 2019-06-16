# start
```py
import cv2

def cv2ShowImages(imgs):
    for i,img in enumerate(imgs):
        cv2.namedWindow(str(i),cv2.WINDOW_NORMAL)
        cv2.imshow(str(i),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


```

# 阈值化
cv2.threshold(a.astype('uint8'),5,255,cv2.THRESH_BINARY_INV)
cv2.THRESH_BINARY 将大约阈值的变为255,小于的变为0
cv2.THRESH_BINARY_INV 相反


# Image Processsing
## Filtering
### filter2D()
 Non-separable linear filter
### sepFilter2D()
Separable linear filter
### boxFilter()
Smooth the image with one of the linear or non-linear filters
### GaussianBlur()
### medianBlur()
### bilateralFilter()

### Sobel(), Scharr()
Compute the spatial image derivatives
### Laplacian()
 compute Laplacian: ∆I = @x @2I2 + @y @2I 2
### erode(), dilate()
Morphological operations

Example. Filter image in-place with a 3x3 high-pass kernel
(preserve negative responses by shifting the result by 128):
filter2D(image, image, image.depth(), (Mat_<float>(3,3)«
-1, -1, -1, -1, 9, -1, -1, -1, -1), Point(1,1), 128)

## Geometrical Transformations
### resize()
Resize image
### getRectSubPix()
Extract an image patch
### warpAffine()
Warp image affinely
### warpPerspective()
 Warp image perspectively
### remap()
Generic image warping
### convertMaps()
Optimize maps for a faster remap() execution
Example. Decimate image by factor of p2:
Mat dst; resize(src, dst, Size(), 1./sqrt(2), 1./sqrt(2))

## Various Image Transformations
### cvtColor()
Convert image from one color space toanother
### threshold(),
### adaptivethreshold()
Convert grayscale image to binary image
using a fixed or a variable threshold
### floodFill()
 Find a connected component using region growing algorithm
### integral()
Compute integral image
### distanceTransform()
build distance map or discrete Voronoi
diagram for a binary image.
### watershed(),
### grabCut()
marker-based image segmentation algorithms. See the samples watershed.cpp
and grabcut.cpp.


```python
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    #capture frame-by-frame
    ret , frame = cap.read()

    #our operation on the frame come here
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    #display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) &0xFF ==ord('q'):  #按q键退出
        break
#when everything done , release the capture
cap.release()
cv2.destroyAllWindows()
```

# cv2.filter2D


# cv2.cvtColor
颜色转换
cv2.COLOR_RGB2GRAY
cv2.COLOR_RGB2HSV

# gimg.ravel
plt.hist(gimg.ravel(),256,[0,256]); plt.show()

# cv2.calcHist
直方图数据
```python
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
```


# 多个窗口 多个图像
```python
cv2.namedWindow('image1',cv2.WINDOW_NORMAL)
cv2.imshow('image1',img3)
cv2.namedWindow('image2',cv2.WINDOW_NORMAL)
cv2.imshow('image2',cImg3.astype('uint8'))
cv2.waitKey(0)
cv2.destroyAllWindows()
```


```python
def cv2ShowImages(imgs):
    for i,img in enumerate(imgs):
        cv2.namedWindow(str(i),cv2.WINDOW_NORMAL)
        cv2.imshow(str(i),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```


uint8


# version
cv2.__version__


# Simple GUI (highgui module)
## namedWindow(winname,flags)
 Create named highgui window
## destroyWindow(winname)
 Destroy the specified window
## imshow(winname, mtx)
 Show image in the window
## waitKey(delay)
 Wait for a key press during the specified time interval (or forever). Process
events while waiting. Do not forget to
call this function several times a second
in your code.
## createTrackbar(...)
 Add trackbar (slider) to the specified
 window
## setMouseCallback(...)
Set the callback on mouse clicks and
movements in the specified window
See camshiftdemo.cpp and other OpenCV samples on how to
use the GUI functions.


# Matrix Manipulations: Copying,
Shuffling, Part Access
src.copyTo(dst) Copy matrix to another one
src.convertTo(dst,type,scale,shift) Scale and convert to
another datatype
m.clone() Make deep copy of a matrix
m.reshape(nch,nrows) Change matrix dimensions and/or number of channels without copying data
m.row(i), m.col(i) Take a matrix row/column
m.rowRange(Range(i1,i2))
m.colRange(Range(j1,j2))
Take a matrix row/column span
m.diag(i) Take a matrix diagonal
m(Range(i1,i2),Range(j1,j2)),
m(roi)
Take a submatrix
m.repeat(ny,nx) Make a bigger matrix from a smaller one
flip(src,dst,dir) Reverse the order of matrix rows and/or
columns
split(...) Split multi-channel matrix into separate
channels
merge(...) Make a multi-channel matrix out of the
separate channels
mixChannels(...) Generalized form of split() and merge()
randShuffle(...) Randomly shuffle matrix elements
Example 1. Smooth image ROI in-place
Mat imgroi = image(Rect(10, 20, 100, 100));
GaussianBlur(imgroi, imgroi, Size(5, 5), 1.2, 1.2);
Example 2. Somewhere in a linear algebra algorithm
m.row(i) += m.row(j)*alpha;
Example 3. Copy image ROI to another image with conversion
Rect r(1, 1, 10, 20);
Mat dstroi = dst(Rect(0,10,r.width,r.height));
src(r).convertTo(dstroi, dstroi.type(), 1, 0);

# Object Detection
matchTemplate Compute proximity map for given template.
CascadeClassifier Viola’s Cascade of Boosted classifiers using Haar or LBP features. Suits for detecting faces, facial features and some
other objects without diverse textures.
See facedetect.cpp
HOGDescriptor N. Dalal’s object detector using
Histogram-of-Oriented-Gradients
(HOG) features. Suits for detecting people, cars and other objects
with well-defined silhouettes. See
peopledetect.cpp

# Reading video from a file or from a camera
VideoCapture cap;
if(argc > 1) cap.open(string(argv[1])); else cap.open(0);
Mat frame; namedWindow("video", 1);
for(;;) {

    cap » frame; if(!frame.data) break;
imshow("video", frame); if(waitKey(30) >= 0) break;
}


# Importing an Image & Viewing it & save it
```py
import cv2
image = cv2.imread("./Path/To/Image.extension")
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Warning 1: On reading images this way via openCV, it isn’t in RGB colorspace—it’s in BGR. Sometime this won’t be an issue with you, you’ll only have trouble if you want to add something colored to your image.
# There are two solutions:

# Switch the R — 1st one(red) with the B — 3rd one(blue), so that Red is (0,0,255) instead of (255,0,0).
# Change the colorspace to RGB:
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# and go on with your code with rgb_image instead of image.

# Warning 2: To close the window that’s displaying the image, press any button. If you use the close button it may cause freezes (happens to me when I’m on a Jupyter notebook).

# For simplicity, throughout this tutorial I’ll be using this method to view images:
import cv2
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Finally, Saving the image
import cv2
image = cv2.imread("./Import/path.extension")
cv2.imwrite("./Export/Path.extension", image)
```


# Cropping

```py
import cv2
cropped = image[10:500, 500:2000]
viewImage(cropped, "Doggo after cropping.")
# where image[10:500, 500:2000] is image[y:y+h, x:x+w]
```


# Resizing
```py
import cv2
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
viewImage(resized, "After resizing with 20%")
# This resizing function maintains the dimension-ratio of the original image.

```

# Rotating
```py
import cv2
(h, w, d) = image.shape
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
viewImage(rotated, "Doggo after rotation by 190 degrees")
# image.shape outputs the height, width, and channels. M is the rotation matrix—this rotates the image 180 degrees around its center.
# -ve angle rotates the image clockwise & +ve angle rotates the image counterclockwise.
```
# reference
https://heartbeat.fritz.ai/opencv-python-cheat-sheet-from-importing-images-to-face-detection-52919da36433