import googletrans                  #Translation
import speech_recognition as sr     #SpeechRecognition
import gtts                         #TextToSpeech

print("WELCOME TO THE BEST TRANSLATOR! \nLook at the list of languages given below alongwith their language-code \nSelect the language code carefully...")
print("\n",gtts.lang.tts_langs())
sourcelang = input("\nEnter the SOURCE language (language before translation): ")
destin = input("Enter the DESTINATION language (language after translation): ")


#SPEECH-TO-TEXT PART...
r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0)
    #Recognizing Speech
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    result = r.recognize_google(audio)
print(result)



#TRANSLATION PART...
from googletrans import Translator
#print(googletrans.LANGUAGES)
translator = Translator()
t = translator.translate(result, src = sourcelang, dest = destin)
print(t.text)



#TEXT-TO-SPEECH PART...
tts = gtts.gTTS(t.text,lang=destin)
tts.save("saved.mp3")
