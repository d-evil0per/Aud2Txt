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
from os import system

def convert(file,folder,count):
	# print(folder)
	# pass
	file_path=str(file)
	folder_path=str(folder)
	file_details,file_ext=file_path.split('.')
	# file_details=file_details.replace("-","")
	file_details=file_details.replace(" ","")
	# print(file_details)
	file_name=file_details.split("/")
	folder_path=folder_path.split("/")
	system("mkdir wavfiles/"+str(folder_path[-1]))
	# print(file_name[-1])
	new_file="wavfiles/"+folder_path[-1]+"/"+file_name[-1]+".wav"

	sound = AudioSegment.from_mp3(file)
	sound.export(new_file, format="wav")
	print("conversion Complete... ")
	



def recur(folder_path):
	p=Path(folder_path)
	dirs=p.glob("*")
	i=0
	# print(dirs)
	for folder in dirs:
		
		if folder.is_dir():
			print("Processing Folder- "+str(folder))
			recur(folder)
		else:
			print("Converting File- "+str(folder))
			i+=1
			convert(folder,folder_path,i)

def banner():
	system('clear')
	print("`7MMM.     ,MMF'`7MM''''Mq.                   `7MMF'     A     `7MF'      db      `7MMF'   `7MF'")
	print("  MMMb    dPMM    MM   `MM.                    `MA     ,MA     ,V       ;MM:       `MA     ,V  ")
	print("  M YM   ,M MM    MM   ,M9  pd''b.   pd*'*b.    VM:   ,VVM:   ,V       ,V^MM.       VM:   ,V   ")
	print("  M  Mb  M' MM    MMmmdM9  (O)  `8b (O)   j8     MM.  M' MM.  M'      ,M  `MM        MM.  M'   ")
	print("  M  YM.P'  MM    MM            ,89     ,;j9     `MM A'  `MM A'       AbmmmqMA       `MM A'    ")
	print("  M  `YM'   MM    MM          ''Yb.  ,-='         :MM;    :MM;       A'     VML       :MM;     ")
	print(".JML. `'  .JMML..JMML.           88 Ammmmmmm       VF      VF      .AMA.   .AMMA.      VF      ")
	print("                           (O)  .M'                                                            ")
	print("                            bmmmd' ")
	print("================================Created By D-eviloper==========================================")
	print("============================Convert Mp3 file to Wave File======================================")
	print("\n")


banner()
# create output folder
if os.path.exists("wavfiles"):
	pass
else:
	system("mkdir wavfiles")
recur(directory)
# print("Launching Aud2Seg for Segmentation of audio files.")
# print("Please Wait....")
# time.sleep(2)
# system("python3 aud2seg.py wavfiles")


