import speech_recognition as sr
import webbrowser
import pyautogui as pg
import sounddevice as sd
import torch
import threading
import time
import cv2
import mss
import re
from colorama import Fore as C
from time import sleep
import numpy as np
from ctypes import windll, Structure, c_long, byref
from PIL import Image
from Test import *

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000  # 48000
speaker = 'baya'  # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')  # cpu или gpu
model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
#model.to(device)

wb = webbrowser.open_new_tab

def YouTube(sit):
    wb(f'https://www.youtube.com/results?search_query={sit}')
site_yt = 'https://www.youtube.com'
site_yt_serch = 'https://www.youtube.com/results?search_query='

wal = 'C:/Users/makle/OneDrive/Рабочий стол/Voice_Meneger/Переводчик/Predator.txt'

STOP = ['стоп', 'полное выключение', "полное отключение"]
RESTART = ['рестарт', "перезагрузка"]
brk = ['выключись', 'отбой', 'хватит', 'отключение']
yt = ['ютюб', 'открой ютюб', 'видео', 'youtube']
music = ['музыка', 'включи музыку', 'вк']
next_music = ['перелистни музыку', 'следующая', 'перелистни', 'надоела']
back_music = ['верни', 'назад', 'прошлую']
close = ['закрой youtube', 'закрой браузер', 'закрой вк', 'закрой']
site = ['закрой вкладку', 'убери лишнее', 'удали мусор']
hi = ['привет', 'здравствуй', 'приветствую']
soft = ['сверни код']
posit = ['позиция', 'узнать позицию']
Metro_2033 = ['метро', 'запусти метро']
Terraria = ['terraria', 'запустить террарию']
MewnBase = ['мидбас', 'запусти musicbase', 'котик', 'котики', 'запусти котика', 'запусти котиков']
sound_pluse = ['подними громкость', "прибавь громкость", 'повысить громкость', 'прибавь звук', 'повысь звук']
sound_minuse = ['снизь громкость', 'убавь громкость', 'убавить звук', 'снизить звук', 'снизить громкость']
sound = ['громкость', 'звук', 'измени звук', 'измени громкость']
Read_file = ['дневник', "заметка", "запись"]
Reset_file = ['обнули файл', "очисти файл", "сотри файл", 'обнулить файл']
Redactor_img = ['измени размер изображения', 'изменить размер изображения']
Quote = ['цитата']
Proto = ['протокол']
Proto_def = ['проверка протокола']


def va_speak(word):
    audio = model.apply_tts(text=word,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio * audio_vol, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

def VS(word):
    thr_VS = threading.Thread(target=va_speak, args={word}, name='Поток-3')
    thr_VS.start()

def Voice_Meneger_Pack():

    play = True
    R = sr.Recognizer()

    while play:

        print (audio_vol)

        def listen():
            try:
                global text
                with sr.Microphone() as mic:
                    global text
                    text = None
                    R.energy_treshold = 300
                    R.pause_threshold = 0.5
                    R.phrase_time_limit = 0.5
                    audio = R.listen(mic)
                    text = R.recognize_google(audio, language='ru-RU')
                    text = text.lower()
                    print('Вы произнесли: ' + text)
                    R.adjust_for_ambient_noise(mic, duration=0.5)

            except sr.UnknownValueError:
                pass

        listen()

        def Terraria_Bot():

            class POINT(Structure):
                _fields_ = [("x", c_long), ("y", c_long)]

            def queryMousePosition():
                pt = POINT()
                windll.user32.GetCursorPos(byref(pt))
                return {"x": pt.x, "y": pt.y}

            def click():
                pg.mouseDown()
                time.sleep(0.01)
                pg.mouseUp()

            # 800x600 game window (based on 3440x1440 screen resolution)
            # mon = {"top": 420, "left": 1320, "width": 800, "height": 600}

            title = "Terraria Auto-Fishing"
            sct = mss.mss()

            print("STARTING after 15 seconds, please adjust your rod!")
            time.sleep(15)
            print("Started ...")

            click()
            print("Rod dropped ...")
            last_time = time.time()  # time last fish was catched

            terraria_bot = True

            while terraria_bot:
                if text == 'остановка бота':
                    print('Бот остановлен')
                    terraria_bot = False
                # must be at least 2 seconds before last catch
                if time.time() - last_time < 2:
                    continue

                cur = queryMousePosition()
                mon = {"top": cur['y'] - 5, "left": cur['x'] - 5, "width": 10, "height": 10}
                img = np.asarray(sct.grab(mon))

                # cv2.imshow(title, img)
                # if cv2.waitKey(25) & 0xFF == ord("q"):
                #   cv2.destroyAllWindows()
                #   quit()

                # create hsv
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                # define masks
                # lower mask (0-10)
                lower_red = np.array([0, 50, 50])
                upper_red = np.array([10, 255, 255])
                mask0 = cv2.inRange(hsv, lower_red, upper_red)

        def Translator():
            translator = Translator()
            start = 0

            wal = 'C:/Users/makle/OneDrive/Рабочий стол/Voice_Meneger/Переводчик/Predator.txt'

            with open(wal, 'r', encoding="utf-8") as f:
                input_text = f.read()

            pattern = re.compile(r'\+(.*?)\+')

            output_text = input_text
            for match in input_text.split('='):
                sleep(1)
                start += 1
                translated = translator.translate(match, src='en', dest='ru').text
                output_text = output_text.replace(match, translated)
                print(C.LIGHTCYAN_EX + 'Идёт перевод строки...')
                print(C.CYAN + match, '    ---->    ', C.CYAN + translated, '\n')

            #  print(output_text)

            with open(wal, 'w', encoding="utf-8") as f:
                f.write(output_text)

        if text != None:
            Rite_2 = '+'.join(text.split()[2:])
            Rite_1 = '+'.join(text.split()[1:])
            thr_TB = threading.Thread(target=Terraria_Bot, name='Поток-2')

        for val in RESTART:
            if text == val:
                os.system(f'shutdown /r /t 5')

        for val in STOP:
            if text == val:
                os.system(f'shutdown /s /t 5')

        for val in brk:
            if text == val:
                VS('Отключаюсь')
                print(f'Отключаюсь...')
                play = False

        for val in hi:
            if text == val:
                VS('Здравствуйте')
                print(f'Здравствуйте!')

        for val in yt:
            if text != None:
                if val in text:
                    if len(text.split()) == 1:
                        wb(site_yt)
                    elif len(text.split()) == 2:
                        if text.split()[0] == 'ютюб' or text.split()[0] == 'youtube':
                            YouTube(Rite_1)
                            print('Поиск: ' + Rite_1)
                        else:
                            wb(site_yt)
                    elif len(text.split()) > 2:
                        if text.split()[0] == 'ютюб' or text.split()[0] == 'youtube':
                            YouTube(Rite_1)
                            print('Поиск: ' + Rite_1)
                        elif text.split()[1] == 'ютюб' or text.split()[1] == 'youtube':
                            YouTube(Rite_2)
                            print('Поиск: ' + Rite_2)

        for val in close:
            if text == val:
                VS('приступаю к закрытию')
                print(f'приступаю к закрытию...')
                pg.leftClick(1579, 16)

        for val in site:
            if text == val:
                pg.leftClick(267, 20)
                VS('вкладка закрыта')
                print(f'вкладка закрыта')

        for val in music:
            if text == val:
                wb(site_vk)
                time.sleep(8)
                pg.leftClick(1591, 454)  # 1584 383
                time.sleep(2)
                pg.leftClick(593, 439)  # 457 877

        for val in next_music:
            if text == val:
                pg.leftClick(812, 108)
                word = 'Готово'
                VS(word)
                print(f'Готово')

        for val in back_music:
            if text == val:
                pg.leftClick(752, 100)
                word = 'Готово'
                VS(word)
                print(f'Готово')

        for val in sound_minuse:
            if text == val:
                RK = 10  # int(text[-2:])
                RR = RK*655
                os.system(f'nircmd.exe changesysvolume -{RR}')
                word = 'звук опущен на 10'
                VS(word)
                print(f'звук опущен на 10')

        for val in sound_pluse:
            if text == val:
                RK = 10  # int(text[-2:])
                RR = RK*655
                os.system(f'nircmd.exe changesysvolume +{RR}')
                word = 'звук поднят на 10'
                VS(word)
                print('звук поднят на 10')

        for val in sound:
            if text != None:
                if val in text:
                    RD = int(text.split()[-1])
                    RR = RD * 655
                    os.system(f'nircmd.exe setsysvolume 0')
                    os.system(f'nircmd.exe changesysvolume +{RR}')
                    VS(f'Громкостьо изменена на {str(RR)}')

        for val in posit:
            if text == val:
                print(pg.position())

        for val in soft:
            if text == val:
                pg.leftClick(1474, 24)

        for val in Metro_2033:
            if text == val:
                VS('Запускаю Метро Ласт Лайт')
                wb(Metro)

        for val in Terraria:
            if text == val:
                VS('Запускаю Террарию')
                wb(Terraria_start)

        for val in MewnBase:
            if text == val:
                VS('Запускаю MewnBase')
                wb(MewnBase_start)

        for val in Read_file:
            if text != None:
                if val in text:
                    number = text.split()[-1]
                    f = open(f'C:/Users/makle/OneDrive/Рабочий стол/Voice_Meneger/Notes/Заметка_{number}.txt', 'r', encoding="utf-8")
                    VS(f.read())
                    print(f.read())
                    f.close()

        for val in Redactor_img:
            if text == val:
                print('Файл обнаружен')
                N6 = input("Какой размер установить файлу?(x y): ")
                weight, height = N6.split()
                image = Image.open('C:/Users/makle/OneDrive/Рабочий стол/Voice_Meneger/Редактор/png.jpg').resize((int(weight), int(height)))
                image.show()
                image.save('C:/Users/makle/OneDrive/Рабочий стол/Voice_Meneger/Редактор/png2.jpg')

        for val in Proto:
            if text != None:
                if val in text:
                    print(' '.join(text.split()[1:]))
                    if ' '.join(text.split()[1:]) == 'terraria bot':
                        thr_TB.start()
                    if ' '.join(text.split()[1:]) == 'переводчик':
                        Translator()

        for val in Proto_def:
            if text == val:
                print(thr_TB.is_alive())
                if thr_TB.is_alive() == False:
                    VS('Протокол неактивен')
                elif thr_TB.is_alive() == True:
                    VS('Протокол активен')

        for val in Quote:
            if text != None:
                if val in text:
                    if int(text.split()[-1]) == 1:
                        VS('Живём один раз, надо бы его запомнить')
                    elif int(text.split()[-1]) == 2:
                        VS('Изменяя своей второй половине мы изменяем прежде всего сво+им чувствам')
                    else:
                        VS('Цитата не распознана')
                        print('Цитата не распознана')


def VSP():
    thr_VSP = threading.Thread(target=Voice_Meneger_Pack, name='Поток-3', daemon=True)
    thr_VSP.start()

ui = Ui_MainWindow()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    audio_vol = ui.audio_vol
    VSP()
    VS("Готова к работе")
    sys.exit(app.exec_())

