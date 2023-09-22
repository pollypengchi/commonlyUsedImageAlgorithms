# 錄製固定秒數的影片(ex:錄30s)，並以時間作為檔名，存在特定路徑下

import cv2
import time

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
savePath = 'D:/coding/E2_takePic/saveVideoPath/'
dateAndTime = time.strftime("%Y_%m_%d-%H_%M_%S")
startTime = time.time()
out = cv2.VideoWriter(savePath+dateAndTime+'.avi', fourcc, fps, (width, height))

counter = 0
while counter < fps * 10: #最後的數值為設定的秒數
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('cap', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    counter += 1

cap.release()
out.release()
cv2.destroyAllWindows()