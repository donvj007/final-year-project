import sys
import cv2
import call
import mailSend
import alert

import numpy as np
class Cctv:
    
    print("start")
    
    def __init__(self):
        Cctv.execute()
    def execute():
        cap = cv2.VideoCapture('videoplayback.mp4')
       # cap = cv2.VideoCapture('3.mp4')
        #cap = cv2.VideoCapture('ManWithDog.mp4')

        print("1")
        ret, frame1 = cap.read()
        print("2")
        ret, frame2 = cap.read()
        print("3")
        count = 0
        i=0
        try:
            while cap.isOpened():
                #print("4")
                diff = cv2.absdiff(frame1, frame2)
                #diff = cv2.absdiff(frame1, frame2.astype(np.float64))
                #foo = cv2.subtract(frame1, frame2, dtype=cv2.CV_64F)
                #diff = np.abs(foo, out=foo)
                #print("5")

                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (5,5), 0)
                _, thresh = cv2.threshold(blur, 20,255,cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh,None,iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)

                    if cv2.contourArea(contour) < 700:
                        continue

                    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                                  1, (0, 0, 255), 3)
                    count = count+1
                    if(count == 50):
                        print(count)
                        cv2.imwrite('img'+str(i)+'.jpg',frame1)
                        #mailSend.mSend()
                        #call.calling()
                        alert.makeAlert()
                        
                        i +=1
                        break
                    #print(count)

                # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

                cv2.imshow("feed", frame1)
                frame1 = frame2
                ret, frame2 = cap.read()
                if cv2.waitKey(20) == 27:
                    # cv2.destroyAllWindows()
                    # exit()
                    print("vijay")
                    break
                
                
            cv2.destroyAllWindows()
            print("last")
            cap.release()
        except:
            cv2.destroyAllWindows()
            print("last")
            cap.release()
            #print("error")

           # print("end")
obj = Cctv()
