import cv2
import numpy as np

# Function #
def draw_Circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(flippedimage, (x, y), 10, (0, 0, 255), 4)



cv2.namedWindow(winname='Canvas')
cv2.setMouseCallback('Canvas', draw_Circle)
img = cv2.imread('../DATA/dog_backpack.jpg')
fixed_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
flippedimage = cv2.flip(fixed_image,-1)


while True:
    cv2.imshow('Canvas', flippedimage)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()