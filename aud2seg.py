# from pydub import AudioSegment
# sound = AudioSegment.from_mp3("sos1.mp3")
# sound.export("sos1.wav", format="wav")
#!/usr/bin/python
from PIL import Image
from pydub import AudioSegment
import os
import sys,time
from pathlib import Path
import imghdr
directory = sys.argv[1]


def segment(file,folder,count):
	os.system("mkdir "+str(folder)+"/parts")
	parts=str(folder)+"/parts/out%09d.wav"
	os.system("ffmpeg -i "+str(file)+" -f segment -segment_time 30 -c copy "+parts+"> /dev/null 2>&1")
	print(str(file)+" segmentation Done...")
	
	



def recur(folder_path):
	p=Path(folder_path)
	dirs=p.glob("*")
	i=0
	for folder in dirs:
		# print(folder)
		if folder.is_dir():
			print("Processing Folder- "+str(folder))
			recur(folder)
		else:
			print("Segmenting File- "+str(folder))
			i+=1
			segment(folder,folder_path,i)
def banner():
	os.system('clear')
	print("                                 ,,                                        ")
	print('      db                       `7MM            .M"""bgd                    ')
	print('     ;MM:                        MM           ,MI    "Y                    ')
	print('    ,V^MM.    `7MM  `7MM    ,M""bMM   pd*"*b. `MMb.      .gP"Ya   .P"Ybmmm ')
	print("   ,M  `MM      MM    MM  ,AP    MM  (O)   j8   `YMMNq. ,M'   Yb :MI  I8   ")
	print('   AbmmmqMA     MM    MM  8MI    MM      ,;j9 .     `MM 8M""""""  WmmmP"   ')
	print("  A'     VML    MM    MM  `Mb    MM   ,-='    Mb     dM YM.    , 8M        ")
	print(".AMA.   .AMMA.  `Mbod'YML. `Wbmd'MML.Ammmmmmm P;Ybmmd'   `Mbmmd'  YMMMMMb  ")
	print("                                                                 6'     dP ")
	print("                                                                 Ybmmmd'   ")
	print("================================Created By D-eviloper==========================================")
	print("=============================Breaks Audio files into Segments======================================")
	print("\n")


banner()

recur(directory)
# print("Launching Aud2txt To Transcribe the audio files.")
# print("Please Wait....")
# time.sleep(2)
# os.system("python3 aud2txt.py wavfiles")

