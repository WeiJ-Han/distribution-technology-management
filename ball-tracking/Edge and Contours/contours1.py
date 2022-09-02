import cv2
import numpy as np
#讀入相片檔案
image = cv2.imread("contours1.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blurred = cv2.GaussianBlur(gray, (11, 11), 0)
#binaryIMG = cv2.Canny(blurred, 20, 160)

(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#(cnts, _) = cv2.findContours(binaryIMG.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)

for c in cnts:        
        mask = np.zeros(gray.shape, dtype="uint8")  #依Contours圖形建立mask
        cv2.drawContours(mask, [c], -1, 255, -1) #255 →白色, -1→塗滿

        # show the images
        cv2.imshow("Image", image)
        cv2.imshow("Mask", mask)

#將mask與原圖形作AND運算
        cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))  
        cv2.waitKey(0)
cv2.destroyAllWindows() 


