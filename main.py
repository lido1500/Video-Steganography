import os
from subprocess import call, STDOUT

import cv2 as cv
from stegano import lsb

from encdec import encoding, decoding
from extraction import video, audio

ext_vid = video
ext_aud = audio
encode = encoding


def final_stitching(frame_path, audio_path):
    # Stitch frames together
    call(["ffmpeg", "-i", frame_path + "%d.png", "-vcodec", "png", frame_path + "video.mp4", "-y"],
         stdout=open(os.devnull, "w"),
         stderr=STDOUT)

    # Add audio to video
    call(
        ["ffmpeg", "-i", frame_path + "video.mp4", "-i", audio_path + "audio.mp3", "-codec", "copy",
         frame_path + "video.mp4", "-y"],
        stdout=open(os.devnull, "w"), stderr=STDOUT)


def final_decoding(frame_direc):
    return ''


# This is from where the program execution begins
if __name__ == '__main__':
    # Initialize a temp directory to store video frames and provide a path
    temp_folder = '/Users/tchiringlama/extraction/video_frames/'
    embed_message = 'THIS_IS_A_SECRET_MESSAGE'

    audio_store = '/Users/tchiringlama/extraction/audio/'

    # audio = '/Users/tchiringlama/PycharmProjects/Video-Steganography/'
    audio = '/Users/tchiringlama/airplane.mp4'
    store = '/Users/tchiringlama/extraction/audio/'

    # Extracts frames from video and store in a directory
    # ext_vid.create_frames(temp_folder)
    # ext_aud.extract_audio(audio, store)

    # encode.encode_string(input_string=embed_message, root=temp_folder)

    # Encode message and create video
    # final_stitching(frame_path=temp_folder, audio_path=audio_store)

    # Decrypt frames and display secret
    decode = decoding
    decode.decode_string(temp_folder)
