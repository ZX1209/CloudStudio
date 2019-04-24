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