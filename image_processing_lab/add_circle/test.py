import cv2 
import numpy as np 
img = cv2.imread('sample.jpg')

height, width = img.shape[:2]

distance = 50 

num_arcs = int((height + width) / distance)

for i in range(num_arcs):
    start_point = (i * distance, height - i * distance)
    end_point = (width - i * distance, 0 + i * distance)
    print(start_point, end_point)
    cv2.ellipse(img, start_point, end_point, 0, 180, (0, 0, 255), 2)

    cv2.imshow('Arcs', img)
    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()