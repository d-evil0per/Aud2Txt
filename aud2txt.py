from PIL import Image
from pydub import AudioSegment
import os
import sys
from pathlib import Path
import imghdr
import speech_recognition as sr
from tqdm import tqdm


directory = sys.argv[1]





def convert(file,folder,pack,count):
	with open("api-key.json") as f:
		GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()
	r = sr.Recognizer()
	files = sorted(os.listdir(str(file)+'/'))
	all_text = []
	for f in tqdm(files):
		name = str(file)+'/' + f
		print("Transcribing File- "+str(name))
		with sr.AudioFile(name) as source:
			audio = r.record(source)
		# text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
		# all_text.append(text)
		try:
			text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
			all_text.append(text)
		except:
			text = "No Audio"
			all_text.append(text)
	transcript = ""
	for i, t in enumerate(all_text):
		total_seconds = i * 30
    	# Cool shortcut from:
    	# https://stackoverflow.com/questions/775049/python-time-seconds-to-hms
    	# to get hours, minutes and seconds
		m, s = divmod(total_seconds, 60)
		h, m = divmod(m, 60)

		total_seconds_n = total_seconds + 30
    	# Cool shortcut from:
    	# https://stackoverflow.com/questions/775049/python-time-seconds-to-hms
    	# to get hours, minutes and seconds
		m_n, s_n = divmod(total_seconds_n, 60)
		h_n, m_n = divmod(m_n, 60)

    	# Format time as h:m:s - 30 seconds of text
		transcript = transcript + "{:0>2d}:{:0>2d}:{:0>2d}-{:0>2d}:{:0>2d}:{:0>2d} {}\n\n".format(h, m, s,h_n, m_n, s_n, t)
		print("Transcript completed- "+str(transcript))
	# print("Transcript Completed...")
	transcript_file=str(folder)+"/"+str(pack)+".txt"
	with open(transcript_file, "w") as f:
		f.write(transcript)

    



def recur(folder_path):
    p=Path(folder_path)
    dirs=p.glob("*")
    i=0
    for folder in dirs:
    	folder_path_str=str(folder)
    	folder_details=folder_path_str.split("/")
    	folder_len=len(folder_details)
    	
    	if folder_details[folder_len-1]!="parts":
    		recur(folder)
    	else:
    		# print(folder_details[folder_len-1])
    		
    		# print(folder_path)
    		i+=1
    		convert(folder,folder_path,folder_details[folder_len-2],i)

        # if folder.is_dir():
            # recur(folder)
        # else:
            # i+=1
            # convert(folder,folder_path,i)
def banner():
	os.system('clear')

	print("                                 ,,                                           ")
	print("      db                       `7MM           MMP##MM##YMM              mm    ")
	print("     ;MM:                        MM           P'   MM   `7              MM    ")
	print("    ,V^MM.    `7MM  `7MM    ,M##bMM   pd*#*b.      MM      `7M'   `MF'mmMMmm  ")
	print("   ,M  `MM      MM    MM  ,AP    MM  (O)   j8      MM        `VA ,V'    MM    ")
	print("   AbmmmqMA     MM    MM  8MI    MM      ,;j9      MM          XMX      MM    ")
	print("  A'     VML    MM    MM  `Mb    MM   ,-='         MM        ,V' VA.    MM    ")
	print(".AMA.   .AMMA.  `Mbod#YML. `Wbmd#MML.Ammmmmmm    .JMML.    .AM.   .MA.  `Mbmo ")
	print("================================Created By D-eviloper==========================================")
	print("================================Converts Audio to Text==========================================")
	print("\n")


banner()
recur(directory)
