import speech_recognition as sr
from pydub import AudioSegment
import shutil

# convertendo tipo de audio para wav
# pode ser usado algum algoritimo com split para pegar a extensao do audio e passar a variavel para o format
sound = AudioSegment.from_file("./midia/WhatsApp Ptt 2023-05-11 at 18.36.12.ogg", format="ogg")
sound.export("teste.wav", format="wav")
shutil.move("./teste.wav", "./midia/teste.wav")

r = sr.Recognizer()

# carregando o arquivo .wav
with sr.AudioFile('./midia/teste.wav') as source:
    audio = r.record(source)

# usando o Google Speech Recognition para transcrever o áudio
try:
    text = r.recognize_google(audio, language='pt-BR')
    print("Texto transcrito:", text)
except sr.UnknownValueError:
    print("Não foi possível transcrever o áudio")
except sr.RequestError as e:
    print("Não foi possível transcrever o áudio; {0}".format(e))
