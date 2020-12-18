import os
import cv2 as cv

vid = cv.VideoCapture('video.mp4')
count = 0
temp_folder = '/Users/pasang/vid_frames'
while vid.isOpened():
    ret, frame = vid.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), frame)
    count += 1
    print(frame.tobytes())
    # video = cv.cvtColor(frame)
    # cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
vid.release()
cv.destroyAllWindows()
