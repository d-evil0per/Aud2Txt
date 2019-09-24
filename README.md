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
                                                                                       
  <pre>                                                                                     
`7MMM.     ,MMF'                             `7MMF'     A     `7MF'                    
  MMMb    dPMM                                 `MA     ,MA     ,V                      
  M YM   ,M MM  `7MMpdMAo.  pd""b.   pd*"*b.    VM:   ,VVM:   ,V    ,6"Yb.  `7M'   `MF'
  M  Mb  M' MM    MM   `Wb (O)  `8b (O)   j8     MM.  M' MM.  M'   8)   MM    VA   ,V  
  M  YM.P'  MM    MM    M8      ,89     ,;j9     `MM A'  `MM A'     ,pm9MM     VA ,V   
  M  `YM'   MM    MM   ,AP    ""Yb.  ,-='         :MM;    :MM;     8M   MM      VVV    
.JML. `'  .JMML.  MMbmmd'        88 Ammmmmmm       VF      VF      `Moo9^Yo.     W     
                  MM       (O)  .M'                                                    
                .JMML.      bmmmd'                                                     

</pre>
python mp32wav.py <folder_name>

To convert all mp3 files inside a folder/subfolder to wav format audio files, It creates wavfiles folder and saves the converted wav files in it.

# Aud2Seg
<pre>
                                 ,,                                        
      db                       `7MM            .M"""bgd                    
     ;MM:                        MM           ,MI    "Y                    
    ,V^MM.    `7MM  `7MM    ,M""bMM   pd*"*b. `MMb.      .gP"Ya   .P"Ybmmm 
   ,M  `MM      MM    MM  ,AP    MM  (O)   j8   `YMMNq. ,M'   Yb :MI  I8   
   AbmmmqMA     MM    MM  8MI    MM      ,;j9 .     `MM 8M""""""  WmmmP"   
  A'     VML    MM    MM  `Mb    MM   ,-='    Mb     dM YM.    , 8M        
.AMA.   .AMMA.  `Mbod"YML. `Wbmd"MML.Ammmmmmm P"Ybmmd"   `Mbmmd'  YMMMMMb  
                                                                 6'     dP 
                                                                 Ybmmmd'   

</pre>
python aud2seg.py <wavfiles_folder>

To Break all the wav audio files inside wavfiles folder/subfolder  into 30 second segments of audio file in wav format,
it will create a parts folder for all subfolders which contains a wav audio files

# Aud2Txt
<pre>
                                 ,,                                           
      db                       `7MM           MMP""MM""YMM              mm    
     ;MM:                        MM           P'   MM   `7              MM    
    ,V^MM.    `7MM  `7MM    ,M""bMM   pd*"*b.      MM      `7M'   `MF'mmMMmm  
   ,M  `MM      MM    MM  ,AP    MM  (O)   j8      MM        `VA ,V'    MM    
   AbmmmqMA     MM    MM  8MI    MM      ,;j9      MM          XMX      MM    
  A'     VML    MM    MM  `Mb    MM   ,-='         MM        ,V' VA.    MM    
.AMA.   .AMMA.  `Mbod"YML. `Wbmd"MML.Ammmmmmm    .JMML.    .AM.   .MA.  `Mbmo 

</pre>

python aud2txt.py <wavfiles_folder>

To generate a Transcribe of all audio segments to a single text file.

