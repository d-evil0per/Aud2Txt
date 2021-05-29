#!/usr/bin/python
import os
from pathlib import Path
directory = r"C:\Users\win 10\Documents\GitHub\Aud2Txt\wavfiles\operating-systems"


def segment(file,folder,org_path):
	
	folder=str(folder)+"\\parts"
	if not os.path.exists(folder):
		os.system("mkdir "+folder)
	parts=str(org_path)+"\\parts\\ut%09d.wav"
	print("ffmpeg -i \""+str(file)+"\" -f segment -segment_time 15 -ac 1 -c copy \""+parts+"\"")
	os.system("ffmpeg -i \""+str(file)+"\" -f segment -segment_time 15 -ac 1 -c copy \""+parts+"\"")
	print(str(file)+" segmentation Done...")
	
	



def recur(folder_path):
	p=Path(folder_path)
	dirs=p.glob("*")
	i=0
	for folder in dirs:
		if folder.is_dir():
			
			print("Processing Folder- "+str(folder))
			recur(folder)
		else:
			print("Segmenting File- "+str(folder))
			i+=1
			new_folder_path=str(folder_path).split("\\")[-2]+"\\"+str(folder_path).split("\\")[-1]
			# print()
			segment(folder,new_folder_path,folder_path)
def banner():
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


