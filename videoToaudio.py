import glob
import os
from moviepy.editor import *

a = glob.glob("*.mp4")
os.system("mkdir myaudio")
for i in a:
	k = i.replace(".mp4","")
	video = VideoFileClip(i)
	audio = video.audio
	audio.write_audiofile("myaudio/{}.mp3".format(k))
