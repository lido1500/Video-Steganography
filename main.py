import os
import cv2 as cv
from stegano import lsb

vid = cv.VideoCapture('video.mp4')


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
        print(frame.tobytes())

        # Display Video in a window
        cv.imshow('frame', frame)
        # Press Q to Exit and Close Window
        if cv.waitKey(1) == ord('q'):
            break
    # Release Video and Close Opened Windows after Video ends.
    vid.release()
    cv.destroyAllWindows()


# Method to Create Frames From Video and Store in a Directory
def store_frame(frames_path, count, each_frame):
    cv.imwrite(os.path.join(frames_path, "{:d}.png".format(count)), each_frame)


# Method to Encrypt Secret into frames, takes two parameters input_string and directory where frames stored
def encode_string(input_string, frame_path):
    f_name = frame_path
    secret_enc = lsb.hide(f_name, input_string)
    secret_enc.save(f_name)
    print("[INFO] frame {} holds {}".format(f_name, input_string))


# Method to Decrypt Secret stored in frames and print secret, takes one parameters i.e directory where frames stored
def decode_string(frame_direc):
    f_name = frame_direc
    secret_dec = lsb.reveal(f_name)
    print("YOUR SECRET MESSAGE: ", secret_dec)


# This is from where the program execution begins
if __name__ == '__main__':
    # Initialize a temp directory to store video frames and provide a path
    temp_folder = '/Users/pasang/vid_frames'
    # Extracts frames from video and store in a directory
    create_frames(temp_folder)

    # Encrypt frames that are stored in the directory
    encode_string("THIS IS A SECRET MESSAGE", temp_folder)

    # Decrypt frames and display secret
    decode_string(temp_folder)
