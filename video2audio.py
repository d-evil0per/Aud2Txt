from moviepy.editor import *

mp4_file = r'C:\Users\win 10\Documents\GitHub\Aud2Txt\videosample\video.mp4'
mp3_file = r'C:\Users\win 10\Documents\GitHub\Aud2Txt\videosample\video.mp3'

videoclip = VideoFileClip(mp4_file)

audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)

audioclip.close()
videoclip.close()