from gtts import gTTS

text = "Giraffe Giraffidae Plant Plant community Vertebrate Ecoregion Green Leaf Neck Natural landscape"
tts = gTTS(text, lang='ko')
tts.save('1.mp3')

