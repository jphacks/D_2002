from outcome_sender import outcome_sender as sender
import cv2, time

img1 = cv2.imread('./image/display_unlocked.jpeg')
img1 = cv2.resize(img1, (640, 480))

img2 = cv2.imread('./image/display_locked.jpeg')
img2 = cv2.resize(img2, (640, 480))

cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)


while(True):
    outcome = sender()
    if outcome:
        cv2.imshow("window", img1)
    else:
        cv2.imshow("window", img2)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
    time.sleep(1)

cv2.destroyWindow("window")