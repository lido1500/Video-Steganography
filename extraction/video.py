import os
import cv2 as cv

# vid = cv.VideoCapture('video.mp4')
vid = cv.VideoCapture('/Users/tchiringlama/airplane.mp4')


# Method to Create Frames
def create_frames(frame_path):
    # Initial variable count
    count_frames = 0
    # Open Video and while Vid is Opened perform Operations
    while vid.isOpened():
        # Read Video Frame by Frame and store in frame Variable
        # Success stores whether or not we got a frame, it is a boolean parameter
        success, frame = vid.read()
        # if frame is read correctly success is True
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Create each frame of video and store in a directory, calls create_frame method
        store_frame(frame_path, count_frames, frame)
        # Increment frame count, this variable counts how many frames are there
        count_frames += 1
        # We can also see frames as bytes
        # print(frame.tobytes())

        # Display Video in a window
        # cv.imshow('frame', frame)
        # Press Q to Exit and Close Window
        # if cv.waitKey(1) == ord('q'):
        #     break
    # Release Video and Close Opened Windows after Video ends.
    vid.release()
    cv.destroyAllWindows()


# Method to Create Frames From Video and Store in a Directory
def store_frame(frames_path, count, each_frame):
    cv.imwrite(os.path.join(frames_path, "{:d}.png".format(count)), each_frame)
