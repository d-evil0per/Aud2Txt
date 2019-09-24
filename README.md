# Aud2Txt
Audio to text using Google Speech Recognition API

# Note
You need to Create API KEY For google Speech Recogination Cloud API From https://console.developers.google.com and download the json credentials into your project folder and rename it as api-key.json 

# Requirements:
	  1.google-api-python-client==1.6.4
  	2.httplib2==0.10.3
  	3.oauth2client==4.1.2
  	4.pyasn1==0.4.2
  	5.pyasn1-modules==0.2.1
  	6.rsa==3.4.2
  	7.six==1.11.0
  	8.SpeechRecognition==3.8.1
  	9.tqdm==4.19.5
  	10.uritemplate==3.0.0
  	11.pydub
 # Run the pip install -r requirement.txt to install all these requirement through pip


# Steps:
	1.Mp32Wav (convert mp3 to wav)
	2.Aud2Seg (Break audio into segments)
	3.Aud2Txt (Convert segmented audio to TXT)


# Mp32Wav 
python mp32wav.py <folder_name>

To convert all mp3 files inside a folder/subfolder to wav format audio files, It creates wavfiles folder and saves the converted wav files in it.

# Aud2Seg
python aud2seg.py <wavfiles_folder>

To Break all the wav audio files inside wavfiles folder/subfolder  into 30 second segments of audio file in wav format,
it will create a parts folder for all subfolders which contains a wav audio files

# Aud2Txt
python aud2txt.py <wavfiles_folder>

To generate a Transcribe of all audio segments to a single text file.

