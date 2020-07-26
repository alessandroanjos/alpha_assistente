import speech_recognition as sr
import webbrowser 
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:

        if ask:
            #print(ask)
            alpha_speak(ask)

        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio, None, 'pt-br')
        except sr.UnknownValueError:
            alpha_speak('Desculpe, eu não entendi isso')
        except sr.RequestError:
            alpha_speak('Desculpe, meu serviço de fala está inoperante')
        return voice_data

def alpha_speak(audio_string):
    tts = gTTS(text=audio_string, lang='pt-br')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'Qual o seu nome' in voice_data:
        alpha_speak("Meu nome é Alpha")

    if 'Que hora é agora' in voice_data:
        alpha_speak(ctime())

    if 'pesquisar' in voice_data:
        search = record_audio('O que você quer procurar?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alpha_speak('Aqui é o que eu encontrei para '+ search)

    if 'encontrar uma localização' in voice_data:
        location = record_audio('Qual a localização')
        url = 'https://google.com/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        alpha_speak('Aqui é o a localizacao para '+ location)

    if 'sair' in voice_data:
        alpha_speak('Tudo bem, estou encerrando por aqui')
        exit()


time.sleep(1)
alpha_speak('Como posso ajudar?')

while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)