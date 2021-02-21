import os
from subprocess import call, STDOUT


def extract_audio(path_audio, path_store):
    call(["ffmpeg", "-i", path_audio, "-q:a", "0", "-map", "a",
          path_store + "audio.mp3", "-y"],
         stdout=open(os.devnull, "w"),
         stderr=STDOUT)

# if __name__ == '__main__':
#     audio = '/Users/tchiringlama/PycharmProjects/Video-Steganography/video.mp4'
#     store = '/Users/tchiringlama/extraction/audio/'
#     extract_audio(audio, store)
