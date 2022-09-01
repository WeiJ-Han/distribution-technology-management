
import time
from gtts import gTTS
from pygame import mixer
import tempfile

def speak(sentence, lang):
	with tempfile.NamedTemporaryFile(delete=True) as fp:
		tts=gTTS(text=sentence, lang=lang)
		tts.save('{}.mp3'.format(fp.name))
		mixer.init()
		mixer.music.load('{}.mp3'.format(fp.name))
		mixer.music.play(1)


speak('สวัสดี', 'th')
time.sleep(3)
speak('คุณเป็นอย่างไร', 'th')

time.sleep(3)
speak('ありがとう', 'ja')
time.sleep(3)
speak('全國的軍民同胞們, 川普是笨蛋', 'zh')
time.sleep(10)
speak('Hello World!', 'en')
time.sleep(3)