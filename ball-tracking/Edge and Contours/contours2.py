import cv2

#讀入相片檔案
image = cv2.imread("contours2.png")

#先使用之前提過的Median Blur方法模糊化
final0 = cv2.medianBlur(image, 25)

#轉為灰階：
final = cv2.cvtColor(final0, cv2.COLOR_BGR2GRAY)

#使用Canny方法取邊緣，,不過後方的兩個上下限參數值大小需要多試幾次才能確定。
edged = cv2.Canny(final, 10, 150)

#依據Canny邊緣得到Contours：
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


#依序處理每個Contour
for index, c in enumerate(cnts):
    #計算周長
    peri = cv2.arcLength(c, True)

    #取得Contour Approximation
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)

    #計算面積
    area = cv2.contourArea(c)

    #取得x, y座標點及width, height
    (x, y, w, h) = cv2.boundingRect(approx)

    #顯示相關資訊
    print("index: {}, original: {}, approx: {}, o/a: {},  w: {}, h: {}, area: {}".format(index, len(c), len(approx), str(len(c)/len(approx)), w, h, area))

    #繪出輪廓線
    cv2.drawContours(image, [approx], -1, (0, 255, 0), 1)

    #在Contour位置顯示其編號
    cv2.putText(image, str(index), (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (4, 4, 253), 2)

# 顯示結果
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
