import os
from pathlib import Path
from google.cloud import speech_v1 as speech

directory = r"C:\Users\win 10\Documents\GitHub\Aud2Txt\wavfiles\operating-systems"

def speech_to_text(config, audio):
	client = speech.SpeechClient()
	operation  = client.long_running_recognize(config=config, audio=audio)
	response = operation.result(timeout=90)
	text_res=print_sentences(response)
	return text_res


def print_sentences(response):
	for result in response.results:
		best_alternative = result.alternatives[0]
		transcript = best_alternative.transcript
		confidence = best_alternative.confidence
		print("-" * 80)
		print(f"Transcript: {transcript}")
		print(f"Confidence: {confidence:.0%}")
		
		return transcript


def convert(file,folder,pack):
	
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="api-key.json"
	files = sorted(os.listdir(str(file)+'/'))
	all_text = []
	for f in files:
		name = str(file)+'/' + f
		print("Transcribing File- "+str(name))
		with open(name, "rb") as audio_file:
			content = audio_file.read()
		try:
			config = speech.RecognitionConfig(encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,language_code="en-US")
			audio = speech.RecognitionAudio(content=content)
			text =speech_to_text(config, audio)
			all_text.append(text)
		except Exception as e:
			print(e)
			text = "No Audio"
			all_text.append(text)
	transcript = ""
	for i, t in enumerate(all_text):
		total_seconds = i * 15
		m, s = divmod(total_seconds, 60)
		h, m = divmod(m, 60)

		total_seconds_n = total_seconds + 15
		m_n, s_n = divmod(total_seconds_n, 60)
		h_n, m_n = divmod(m_n, 60)

		transcript = transcript + "{}\n{:0>2d}:{:0>2d}:{:0>2d},000 --> {:0>2d}:{:0>2d}:{:0>2d},000\n {}\n\n".format(i+1,h, m, s,h_n, m_n, s_n, t)
		print("Transcript completed- "+str(transcript))
	transcript_file=str(folder)+"/"+str(pack)+".srt"
	with open(transcript_file, "w") as f:
		f.write(transcript)


def recur(folder_path):
	p=Path(folder_path)
	dirs=p.glob("*")
	i=0
	
	for folder in dirs:
		folder_path_str=str(folder)
		# print(folder_path_str)
		folder_details=folder_path_str.split("\\")
		
		folder_len=len(folder_details)
		
		if folder_details[folder_len-1]!="parts":
			pass
		else:
			convert(folder,folder_path,folder_details[folder_len-2])
			
def banner():
	# os.system('cls')

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



if __name__ == "__main__":
	banner()
	recur(directory)



