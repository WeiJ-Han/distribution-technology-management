
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

speak("國立勤益科技大學", 'zh')
time.sleep(5)

speak("藝人吳宗憲說，施打流感疫苗後出現暈眩的後遺症，亦有民眾反映，小孩接種流感疫苗後有頻尿現象。", 'zh')
time.sleep(12)

speak("疾管署防疫醫師林詠青解釋，雖然流感疫苗的仿單上有載明，接種後有可能出現暈眩症狀，", 'zh')
time.sleep(12)

speak("但目前並無研究證實兩者關聯性，至於小兒頻尿原因很多，很可能是泌尿道感染所致。", 'zh')
time.sleep(12)




