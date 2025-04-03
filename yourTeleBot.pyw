# Welcome in code of YourTeleBot!
# Author: t.me/qpikzzbot
# License: CC BY
# font: Dimkin, author: Dimitri Antonov
# - - -
# Have a nice day, take care ok yourself!
        

# Цвета, используемые в интерфейсе
# Colors < для поиска (см документацию (tl/(yourLang)/manual.html)

black = "#28262A"
darkBlue = "#02000A"
darkGreen = "#2E5D42"
green = "#6A9A85"
grey = "#A1A4A8"
white = "#F5F5F5"

# Открытие и применение настроек
import webbrowser
import subprocess
import json
import os

def openData():
    global tempValue
    data = {}
    
    with open("data/settings","r",-1,"utf-8") as file:
        data["settings"] = json.load(file)

    for i in os.listdir("tl"):
        if i == "none":
            continue
        
        data[i] = {}
        for j in os.listdir("tl/"+i):
        
            try:
                with open(f"tl/{i}/{j}","r",-1,"utf-8") as file:
                    data[i][j.split(".")[0]] = json.load(file)
            except Exception as e:
                tempValue = f"errorOpenData--{e}"
    return data

tempValue = ""
data = openData()
lang = data["settings"]["language"]
consoleMessage = ""


# Подключение модулей 
try:
    from moviepy.editor import VideoFileClip
    from datetime import datetime as dt
    from googletrans import Translator
    from tkinter import messagebox
    from PIL import ImageDraw
    import pygetwindow as pgw
    from tkinter import ttk
    import pyautogui as pag
    from gtts import gTTS
    from tkinter import *
    import keyboard as k
    import pandas as pd
    import random as r
    import pillow_heif
    import time as t
    import threading
    import platform
    import requests
    import telebot
    import sqlite3
    import shutil
    import psutil
    import pygame
    import fitz
    import cv2
    import PIL
    import wmi
except ModuleNotFoundError:
    from tkinter import *

    # Создание окна с приветствием
    firstTk = Tk()
    firstTk.geometry("720x480")
    firstTk.title("YourTelebot • Installer")
    firstTk["bg"] = black
    firstTk.resizable(0,0)

    firstTk.iconbitmap("data/images/blackLogo.ico")

    image = PhotoImage(file="data/images/whitelogo.png")
    logo = Label(firstTk,
                 bg=firstTk["bg"],
                 image=image)
    logo.place(x=60, y=144)

    fr = None
    successInstall = False
    installLang = "en"

    def chooseLang():
        global fr
        if fr:
            fr.destroy()
        fr = Frame(firstTk,
               bg=firstTk["bg"],
               width=360,
               height=480)
        fr.place(x=360,y=0)


        l1 = Label(fr,
                bg=firstTk["bg"],
                text="Your language:",
                fg=white,
                font=("Cruinn", 20))
        l1.place(x=95, y=186)

        buttonsY = 229

        def setInstallLang(lang):
            global installLang
            installLang = lang

            about()

        if "ru" in os.listdir("tl"):

            def enterB1(event):
                b1.config(fg=green)
            def leaveB1(event):
                b1.config(fg=grey)

            b1 = Button(fr,
                        bg=black,
                        fg=grey,
                        font = ("Cruinn", 20),
                        text="Русский",
                        bd=0,
                        activebackground=black,
                        activeforeground=green,
                        command=lambda: setInstallLang("ru"))
            b1.place(x=134, y=buttonsY)

            b1.bind("<Enter>", enterB1)
            b1.bind("<Leave>", leaveB1)

            buttonsY += 41
        
        if "en" in os.listdir("tl"):
            def enterB1(event):
                b2.config(fg=white)
            def leaveB1(event):
                b2.config(fg=grey)

            b2 = Button(fr,
                        bg=black,
                        fg=grey,
                        font = ("Cruinn", 20),
                        text="English",
                        bd=0,
                        activebackground=black,
                        activeforeground=green,
                        command=lambda: setInstallLang("en"))
            b2.place(x=144, y=buttonsY)

            b2.bind("<Enter>", enterB1)
            b2.bind("<Leave>", leaveB1)

            buttonsY += 41
        
        if buttonsY == 229:
            errorLang()
    
    def errorLang():
        global fr
        if fr:
            fr.destroy()
        fr = Frame(firstTk,
               bg=firstTk["bg"],
               width=360,
               height=480)
        fr.place(x=360,y=0)

        l1 = Label(fr,
                bg=firstTk["bg"],
                text="Oops!\nNo translations found!\nPlease reinstall the application.",
                fg=white,
                font=("Cruinn", 18),
                justify="left",
                wraplength=280)
        l1.place(x=0, y=140)

        def enterB1(event):
            b1.config(fg=green)
        def leaveB1(event):
            b1.config(fg=grey)

        b1 = Button(fr,
                    bg=black,
                    fg=grey,
                    font = ("Cruinn", 18),
                    text="github",
                    bd=0,
                    activebackground=black,
                    activeforeground=green,
                    command=lambda: webbrowser.open("https://github.com/qpikzz/yourtelebot"))
        b1.place(x=232, y=315)

        b1.bind("<Enter>", enterB1)
        b1.bind("<Leave>", leaveB1)
    
    def about():
        global fr
        if fr:
            fr.destroy()
        fr = Frame(firstTk,
               bg=firstTk["bg"],
               width=360,
               height=480)
        fr.place(x=360,y=0)

        t1 = Text(fr, 
                  height=5, 
                  width=20,
                  bg=black,
                  fg=white,
                  selectbackground=white,
                  selectforeground=black,
                  font = ("Cruinn", 18),
                  bd=0,
                  wrap="word")
        t1.place(x=0,y=144)

        t1.insert(END, "YourTelebot", "bold")
        t1.insert(END, f" - {data[installLang]['system']['about']}")

        t1.tag_configure("bold", font=("Cruinn", 18, "bold"))
        t1.config(state="disabled")


        def enterB1(event):
            b1.config(fg=green)
        def leaveB1(event):
            b1.config(fg=grey)

        b1 = Button(fr,
                    bg=black,
                    fg=grey,
                    font = ("Cruinn", 18),
                    text=data[installLang]["system"]["continue"],
                    bd=0,
                    activebackground=black,
                    activeforeground=green,
                    command=acceptUsAg)
        b1.place(x=173, y=311)

        b1.bind("<Enter>", enterB1)
        b1.bind("<Leave>", leaveB1)

    def acceptUsAg():
        global fr
        if fr:
            fr.destroy()
        fr = Frame(firstTk,
               bg=firstTk["bg"],
               width=360,
               height=480)
        fr.place(x=360,y=0)

        t1 = Text(fr, 
                  height=5, 
                  width=24,
                  bg=black,
                  fg=white,
                  selectbackground=white,
                  selectforeground=black,
                  font = ("Cruinn", 18),
                  bd=0,
                  wrap="word")
        t1.place(x=0,y=144)

        t1.insert(END, data[installLang]['system']['titleAcceptUserAgree']+" \"")
        t1.insert(END, data[installLang]['system']['userAgree'], "link")
        t1.insert(END, "\"")

        def openUsAg(event):
            os.system(f'start "" "tl/{installLang}/user agreement.docx"')

        t1.tag_configure("link", foreground=green)
        t1.tag_bind("link", "<Enter>", lambda e: t1.config(cursor="hand2"))
        t1.tag_bind("link", "<Leave>", lambda e: t1.config(cursor=""))
        t1.tag_bind("link", "<Button-1>", openUsAg)
        t1.config(state="disabled")

        def enterB1(event):
            b1.config(fg=green)
        def leaveB1(event):
            b1.config(fg=grey)

        b1 = Button(fr,
                    bg=black,
                    fg=grey,
                    font = ("Cruinn", 18),
                    text=data[installLang]["system"]["continue"],
                    bd=0,
                    activebackground=black,
                    activeforeground=green,
                    command=downloadModules)
        b1.place(x=173, y=311)
        
        b1.bind("<Enter>", enterB1)
        b1.bind("<Leave>", leaveB1)

    def downloadModules():
        global fr, successInstall
        if fr:
            fr.destroy()
        fr = Frame(firstTk,
               bg=firstTk["bg"],
               width=360,
               height=480)
        fr.place(x=360,y=0)

        t1 = Text(fr, 
                  height=5, 
                  width=24,
                  bg=black,
                  fg=white,
                  selectbackground=white,
                  selectforeground=black,
                  font = ("Cruinn", 18),
                  bd=0,
                  wrap="word")
        t1.place(x=0,y=144)

        t1.insert(END, data[installLang]["system"]["download"])
        t1.config(state="disabled")

        c = Canvas(fr,
                   width=350,
                   height=30,
                   bg=black,
                   highlightthickness=0)
        c.place(x=0,y=316)

        cVar = DoubleVar(value=0)
        BAR_WIDTH = 300
        BAR_HEIGHT = 20
        BORDER_RADIUS = 10

        def draw_rounded_rect(x, y, width, height, radius, fill):
            c.create_arc(x, y, x + 2 * radius, y + 2 * radius, start=90, extent=90, fill=fill, outline=fill)
            c.create_arc(x + width - 2 * radius, y, x + width, y + 2 * radius, start=0, extent=90, fill=fill, outline=fill)
            c.create_arc(x, y + height - 2 * radius, x + 2 * radius, y + height, start=180, extent=90, fill=fill, outline=fill)
            c.create_arc(x + width - 2 * radius, y + height - 2 * radius, x + width, y + height, start=270, extent=90, fill=fill, outline=fill)
            c.create_rectangle(x + radius, y, x + width - radius, y + height, fill=fill, outline=fill)
            c.create_rectangle(x, y + radius, x + width, y + height - radius, fill=fill, outline=fill)

        def draw_progress(value):
            c.delete("all")

            draw_rounded_rect(25, 5, BAR_WIDTH, BAR_HEIGHT, BORDER_RADIUS, fill=darkBlue) # Фон полосы
                        
            fill_width = int(BAR_WIDTH * value / 100) # Заполненная часть
            if fill_width > 0:
                draw_rounded_rect(25, 5, fill_width, BAR_HEIGHT, BORDER_RADIUS, fill=green)


            firstTk.update()

        for i in ["googletrans==4.0.0-rc1", "pygetwindow", "gtts", "pyautogui", "keyboard", "pywin32", "telebot", "psutil", "pygame", "opencv-python", "wmi", "Pillow", "moviepy==1.0.3", "pillow-heif", "pymupdf", "pandas", "openpyxl"]:
            # os.system(f"pip install {i}")
            subprocess.run(f"pip install {i}", creationflags=subprocess.CREATE_NO_WINDOW)
            if cVar.get() < 100:
                cVar.set(cVar.get() + 6)
                draw_progress(cVar.get())

        successInstall = True
        firstTk.destroy()


    def errorInstall():
        global fr, successInstall
        if fr:
            fr.destroy()
        fr = Frame(firstTk,
               bg=firstTk["bg"],
               width=360,
               height=480)
        fr.place(x=360,y=0)

        l1 = Label(fr,
                bg=firstTk["bg"],
                text=data[installLang]["error"]["install"],
                fg=white,
                font=("Cruinn", 16),
                justify="left",
                wraplength=280)
        l1.place(x=0, y=140)

        def enterB1(event):
            b1.config(fg=green)
        def leaveB1(event):
            b1.config(fg=grey)

        b1 = Button(fr,
                    bg=black,
                    fg=grey,
                    font = ("Cruinn", 18),
                    text=data[installLang]["system"]["helpTitle"],
                    bd=0,
                    activebackground=black,
                    activeforeground=green,
                    command=lambda: webbrowser.open(f"{os.path.dirname(os.path.abspath(__file__))}/tl/{installLang}/dark.html"))
        b1.place(x=232, y=315)

        b1.bind("<Enter>", enterB1)
        b1.bind("<Leave>", leaveB1)

        successInstall = False

    chooseLang()

    firstTk.mainloop()

    try:
        from moviepy.editor import VideoFileClip
        from datetime import datetime as dt
        from PIL import ImageTk, ImageDraw
        from googletrans import Translator
        from tkinter import messagebox
        import pygetwindow as pgw
        from tkinter import ttk
        import pyautogui as pag
        from gtts import gTTS
        from tkinter import *
        import keyboard as k
        import pandas as pd
        import random as r
        import pillow_heif
        import time as t
        import threading
        import platform
        import requests
        import telebot
        import sqlite3
        import shutil
        import psutil
        import pygame
        import fitz
        import cv2
        import PIL
        import wmi
    except:
        firstTk = Tk()
        firstTk.geometry("720x480")
        firstTk.title("YourTelebot • Installer")
        firstTk["bg"] = black
        firstTk.resizable(0,0)

        firstTk.iconbitmap("data/images/blackLogo.ico")

        image = PhotoImage(file="data/images/whitelogo.png")
        logo = Label(firstTk,
                    bg=firstTk["bg"],
                    image=image)
        logo.place(x=60, y=144)

        fr = None
        successInstall = False

        errorInstall()

        firstTk.mainloop()

    if not successInstall:
        quit()


pag.FAILSAFE = False
pillow_heif.register_heif_opener()


# Попытка запуска бота
try: 
    bot = telebot.TeleBot(data["settings"]["token"]) if data["settings"]["token"] else None
except:
    bot = None


# Создание окна
# Create-window <
tk = Tk()
tk.geometry("720x480")
tk.resizable(0, 0)
tk["bg"] = black
tk.iconbitmap("data/images/blackLogo.ico")


# Открытие иконок кнопок показать/скрыть
eye_open = PhotoImage(file="data/images/eye_open.png")
eye_close = PhotoImage(file="data/images/eye_close.png")

try:
    with open("data/splashes.txt","r",-1,"utf-8") as file:
        splash = r.choice(file.read().split("\n"))
    tk.title("YourTeleBot • "+splash)
except:
    tk.title("YourTeleBot • splashes not founded :(")

# Функции
# Установка тегов в сообщение
def setTag(text,message):
    global bot, data
    
    ip = requests.get('https://api.ipify.org?format=json')
    ip = ip.json()["ip"]
    otherInfo =  requests.get(f'https://ipinfo.io/{ip}')

    now = dt.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%d.%m.%Y")

    x,y = pag.position()

    if data["settings"]["hide"]:
        hide = '<span class="tg-spoiler"><b>'
        hideClose = '</b></span>'
    else:
        hide = "<code>"
        hideClose = "</code>"


    # Tags
    replaces = {
        "[ip]":ip,
        "[code]":"<code>","[cod]":"<code>",
        "[/code]":"</code>","[/cod]":"</code>",
        "[b]":"<b>","[bold]":"<b>",
        "[/b]":"</b>","[/bold]":"</b>",
        "[i]":"<i>", "[italic]":"<i>",
        "[/i]":"</i>", "[/italic]":"</i>",
        "[now]":now,
        "[time]":time,
        "[date]":date,
        "[spoiler]":'<span class="tg-spoiler">', "[sp]":'<span class="tg-spoiler">',
        "[/spolier]":"</span>", "[/sp]":"</span>",
        "[x]":x,
        "[y]":y,
        "[n]":"\n",
        "[blockquote]":"<blockquote>","[bq]":"<blockquote>",
        "[/blockquote]":"</blockquote>","[/bq]":"</blockquote>",
        "[h]":hide,"[hide]":hide,
        "[/h]":hideClose,"[/hide]":hideClose,
        "[u]":"<u>", "[underline]":"<u>",
        "[/u]":"</u>", "[/underline]":"</u>",
        "[tempFolder]":data["settings"]["tempFolder"]
        }

    
    if message:
        replaces.update({
            "[user_username]":message.from_user.username,
            "[user_id]":message.from_user.id,
            "[user_first_name]":message.from_user.first_name,
            "[user_last_name]":message.from_user.last_name
        })

    if bot:
        replaces.update({
            "[bot_username]":bot.get_me().username,
            "[bot_id]":bot.get_me().id,
        })

    try:
        otherInfo = otherInfo.json()
        replaces.update({
            "[location]":f"{otherInfo['city']}, {otherInfo['region']}, {otherInfo['country']}",
            "[org]":otherInfo["org"],
            "[timezone]":otherInfo["timezone"]
        })
    except:
        replaces.update({
            "[location]":data[lang]["messages"]["idk"],
            "[org]":data[lang]["messages"]["idk"],
            "[timezone]":data[lang]["messages"]["idk"]
        })
        

    for i in replaces:
        text = text.replace(i,str(replaces[i]))
    return text

# Функция для записи в консоль
def writeInConsole(text):
    global console, data, consoleMessage # Указание консоли
    
    text = setTag(text, None)
    text += "\n"
    consoleMessage += text

# Поток для записи в консоль не зависимо от окна
def consoleWriteText():
    global consoleMessage

    while True:
        if consoleMessage == "":
            t.sleep(1)
            continue
        for i in consoleMessage:
            t.sleep(0.005)
            console.insert(END,i,"padding")
            # tk.update()
            consoleMessage = consoleMessage[1:]

# Ответ бота с скриншотом
def answerWithPic(message, text):
    t.sleep(1.5)
    try:
        screen = pag.screenshot()
        bot.send_photo(message.chat.id,photo=screen,caption=setTag(text,message))
    except:
        bot.send_message(message.chat.id,setTag(text,message))

def mode2mes(bot,message):
    if data["settings"]["2mesMode"]:
        errors = 0
        for i in range(message.id-1,1,-1):
            try:
                bot.delete_message(message.chat.id, i)
                errors = 0
            except:
                errors += 1

            if errors > 7:
                break


# Поток для работы бота не зависимо от других частей программы.
def botFunc():
    global data, bot
    bot = telebot.TeleBot(data["settings"]["token"],parse_mode="html")  


    @bot.message_handler(commands=["start"])
    def start(message):
        if not data["settings"]["botWorking"]:
            return None
        
        user = message.from_user

        log(data[lang]["log"]["useStart"], message)
        mode2mes(bot, message)

        if not data["settings"]["users"]:
            bot.send_message(message.chat.id,setTag(data[lang]["messages"]["start"],message))
            return None
        elif str(user.id) not in data["settings"]["users"]:
            bot.send_message(message.chat.id,setTag(data[lang]["messages"]["start"],message))
        else:
            bot.send_message(message.chat.id,setTag(data[lang]["messages"]["startForUsers"],message))
        

    @bot.message_handler(content_types=["text"])
    def text(message):
        import random as r
        
        if not data["settings"]["botWorking"]:
            return None

        user = message.from_user
        text = message.text
        chat = message.chat

        log(data[lang]["log"]["useCommand"], message)
        mode2mes(bot, message)
        useCommand = True

        if not data["settings"]["users"]:
            bot.send_message(message.chat.id,setTag(data[lang]["messages"]["answerForNotUsers"],message))
            return None
        
        if not (os.path.exists(data["settings"]["tempFolder"]) and os.path.isdir(data["settings"]["tempFolder"])):
            os.mkdir(data["settings"]["tempFolder"])

        if str(user.id) not in data["settings"]["users"]:
            bot.send_message(message.chat.id,setTag(data[lang]["messages"]["answerForNotUsers"],message))
            return None
        
        if chat.type != "private" and not data["settings"]["groups"]:
            bot.send_message(message.chat.id,setTag(data[lang]["messages"]["groupDisable"],message))
            return None

        # Commands_Match
        match text.split()[0].lower():
            case "clear":
                bot.reply_to(message,data[lang]["messages"]["loading"][0])
                
                for i in range(30):
                    tk.update()
                    console.insert(END,f"  {r.randint(0,1)}", "padding")
                    t.sleep(0.003)
                bot.edit_message_text(chat_id=message.chat.id,message_id=message.id+1,text=data[lang]["messages"]["loading"][1])
            
                for i in range(300):
                    tk.update()
                    console.insert(END,f" {r.randint(0,1)}", "padding")
                    t.sleep(0.002)
                    console.see("end")
                bot.edit_message_text(chat_id=message.chat.id,message_id=message.id+1,text=data[lang]["messages"]["loading"][2])

                for i in range(100):
                    tk.update()
                    console.insert(END,f"  {r.randint(0,1)}", "padding")
                    t.sleep(0.001)
                    console.see("end")
                bot.edit_message_text(chat_id=message.chat.id,message_id=message.id+1,text=data[lang]["messages"]["loading"][3])

                for i in range(100):
                    tk.update()
                    console.insert(END," "*r.randint(4,10) + f"{r.randint(0,1)}", "padding")
                    t.sleep(0.001)
                    console.see("end")
                bot.edit_message_text(chat_id=message.chat.id,message_id=message.id+1,text=data[lang]["messages"]["loading"][4])

                for i in range(40):
                    tk.update()
                    console.insert(END,r.choice(["\n"," "*r.randint(1,30)+str(r.randint(0,1))]), "padding")
                    t.sleep(0.001)
                    console.see("end")
                bot.edit_message_text(chat_id=message.chat.id,message_id=message.id+1,text=data[lang]["messages"]["loading"][5])

                for i in range(20):
                    tk.update()
                    console.insert(END,"\n", "padding")
                    t.sleep(0.02)
                    console.see("end")
                bot.edit_message_text(chat_id=message.chat.id,message_id=message.id+1,text=data[lang]["messages"]["loading"][6])


                console.delete("1.0",END)
                writeInConsole(data[lang]["system"]["logo"])
                bot.edit_message_text(chat_id=message.chat.id,message_id=message.id+1,text=data[lang]["messages"]["success"])

            case "ip":
                bot.send_message(chat.id,setTag(data[lang]["messages"]["ip"],message))

            case "screen":
                screen = pag.screenshot()
                bot.send_photo(chat.id, photo=screen, caption=setTag(data[lang]["messages"]["screen"],None))

            case "click":
                pag.click()

                answerWithPic(message,data[lang]["messages"]["click"]) if data["settings"]["answerWithPic"] else bot.send_message(chat.id,setTag(data[lang]["messages"]["click"]))

            case "pos":
                try:
                    screen = pag.screenshot()
                    draw = ImageDraw.Draw(screen)
                    x,y = pag.position()
                    r = 7
                    draw.ellipse((x-r, y-r, x+r, y+r), outline="white", fill="red",width=2)
                    bot.send_photo(chat.id,screen,setTag(data[lang]["messages"]["pos"],None))
                except:
                    bot.send_message(chat.id,setTag(data[lang]["messages"]["posWithoutScreen"]))

            case "press":
                if len(text.split()) != 2:
                    bot.send_message(chat.id,setTag(data[lang]["error"]["press"],message))
                else:
                    pag.press(text.split()[1])
                    
                    answerWithPic(message,data[lang]["messages"]["success"])

            case "write":
                k.write(" ".join(text.split()[1:]))

            case "slowwrite":
                k.write(" ".join(text.split()[1:]),delay=0.1)

            case "create":
                if len(text.split()) == 1:
                    bot.send_message(chat.id,data[lang]["error"]["create"])
                
                elif len(text.split()) == 2:
                    file = text.split()[1]
                    if "\\" not in file:
                        file = f"{data["settings"]["tempFolder"]}/"+file
                    
                    if os.path.exists(file):
                        bot.send_message(chat.id,data[lang]["errors"]["fileHasExists"])
                        return None
                    
                    with open(file,"w") as createFile:
                        bot.send_message(chat.id,setTag(data[lang]["messages"]["create"],message).replace("[file]",file))

                else:
                    file = text.split()[1]
                    if ("\\" not in file) and ("/" not in file):
                        file = f"{data["settings"]["tempFolder"]}/"+file
                    
                    if os.path.exists(file):
                        bot.send_message(chat.id,data[lang]["errors"]["fileHasExists"])
                        return None
                    
                    with open(file,"w",-1,"utf-8") as createFile:
                        createFile.write(" ".join(message.text.split()[2:]))
                        bot.send_message(chat.id,setTag(data[lang]["messages"]["createWithText"],message).replace("[file]",file).replace("[text]"," ".join(message.text.split()[2:])))

            case "mkdir":
                if len(text.split()) < 2:
                    bot.send_message(chat.id,data[lang]["error"]["createfolder"])
                    return None
                
                path = text.split()[1]

                if path.count("/") == 0:
                    path = f"{data["settings"]["tempFolder"]}/"+path

                if os.path.isdir(path):
                    bot.send_message(chat.id,setTag(data[lang]["error"]["isdir"],message).replace("[path]",path))
                    return None
                
                os.mkdir(path)
                bot.send_message(chat.id,setTag(data[lang]["messages"]["createfolder"],message).replace("[path]",path))
                
            case "delete":
                if len(text.split()) < 2:
                    bot.send_message(chat.id,data[lang]["error"]["delete"])
                    return None
                
                file = text.split()[1]
                if file.count(".") == 0:
                    try:
                        shutil.rmtree(file)
                        bot.send_message(chat.id,setTag(data[lang]["messages"]["deletefolder"],message).replace("[path]",file))
                    except FileNotFoundError:
                        bot.send_message(chat.id,data[lang]["error"]["deleteNotFound"])
                    except PermissionError:
                        bot.send_message(chat.id,data[lang]["error"]["permission"])
                    except Exception as e:
                        bot.send_message(chat.id,data[lang]["error"]["deleteUnknown"].replace("[e]",str(e)))
                else:
                    try:
                        os.remove(file)
                        bot.send_message(chat.id,setTag(data[lang]["messages"]["deletefile"],message).replace("[file]",file))
                    except FileNotFoundError:
                        try:
                            shutil.rmtree(file)
                            bot.send_message(chat.id,data[lang]["messages"]["deletefolder"])
                        except FileNotFoundError:
                            bot.send_message(chat.id,data[lang]["error"]["deleteNotFound"])
                        except PermissionError:
                            bot.send_message(chat.id,data[lang]["error"]["permission"])
                        except Exception as e:
                            bot.send_message(chat.id,data[lang]["error"]["deleteUnknown"].replace("[e]",e))
                    except PermissionError:
                        bot.send_message(chat.id,data[lang]["error"]["permission"])
                    except Exception as e:
                        bot.send_message(chat.id,data[lang]["error"]["deleteUnknown"].replace("[e]",str(e)))
            
            case "open":
                if len(text.split()) == 1:
                    bot.send_message(chat,id,data[lang]["error"]["open"])

                else:
                    file = " ".join(text.split()[1:])
                    if not os.path.exists(file):
                        bot.send_message(chat.id,setTag(data[lang]["error"]["fileNotFound"],message).replace("[file]",file))
                        return None
                    
                    os.system(f'start /B "" "{file}"')
                    # subprocess.run(f'start /B "" "{file}"', creationflags=subprocess.CREATE_NO_WINDOW)
                    bot.send_message(chat.id,setTag(data[lang]["messages"]["open"],message).replace("[file]",file))

            case "photo":

                cap = cv2.VideoCapture(0)

                if not cap.isOpened():
                    bot.send_message(chat.id,setTag(data[lang]["error"]["cameraClosed"],message))
                    return None

                ret, frame = cap.read()

                if not ret:
                    pass # потом
                    return
                
                cv2.imwrite(f"{data["settings"]["tempFolder"]}/photo.jpg",frame)
                cap.release()

                image = PIL.Image.open(f"{data["settings"]["tempFolder"]}/photo.jpg")
                bot.send_photo(chat.id,image,setTag(data[lang]["messages"]["photo"],message))
                
            case "apps":
                open_apps = [window.title for window in pgw.getWindowsWithTitle('')] # Прочтение запущенных приложений
                open_apps = [app for app in open_apps if app != '']
                open_apps = "— "+"\n— ".join(open_apps)
                
                active = pgw.getActiveWindow()

                bot.send_message(message.chat.id,setTag(data[lang]["messages"]["apps"],message).replace("[apps]", open_apps).replace("[active]", active.title)) # узнать запущенные программы

            case "knock":
                bot.send_message(message.chat.id,setTag(data[lang]["messages"]["knock"],message))
            
            case "moveto":
                if len(text.split()) != 3:
                    bot.send_message(message.chat.id,setTag(data[lang]["error"]["xynotfound"],message))
                else:
                    pag.moveTo(int(text.split()[1]),int(text.split()[2]))
                    bot.send_message(message.chat.id,setTag(data[lang]["messages"]["moveTo"],message))

            case "moverel":
                if len(text.split()) != 3 and len(text.split()) != 4:
                    bot.send_message(message.chat.id,setTag(data[lang]["error"]["xynotfound"],message))
                elif len(text.split()) == 3:
                    pag.moveRel(int(text.split()[1]),int(text.split()[2]))
                    bot.send_message(message.chat.id,setTag(data[lang]["messages"]["moveTo"],message))
                else:
                    pag.moveRel(int(text.split()[1]),int(text.split()[2]),int(text.split()[3]))
                    bot.send_message(message.chat.id,setTag(data[lang]["messages"]["moveRel"].replace("[t]",int(text.split()[3])),message))

            case "about":
                messageText = setTag(data[lang]["messages"]["about"], message)
                disk = []
                bot.send_message(message.chat.id,setTag(data[lang]["system"]["loading"], message))
                
                try:
                    w = wmi.WMI()
                    for gpu in w.Win32_VideoController():
                        gpuName = gpu.Name
                except:
                    pass

                for i in [
                    ("[node]", platform.node()),
                    ("[user]", os.getlogin()),
                    ("[system]", platform.system()),
                    ("[systemVersion]", str(platform.version())),
                    ("[cpu]", platform.processor()),
                    ("[cpuPercent]", psutil.cpu_percent(interval=5)),
                    ("[videocard]", gpuName),
                    ("[gpu]", round(psutil.virtual_memory().total / (1024 ** 3),2)),
                    ("[gpuPercent]", psutil.virtual_memory().percent),
                    ("[battery]", psutil.sensors_battery().percent),
                    ("[diskCount]",len(psutil.disk_partitions()))
                ]:
                    messageText = messageText.replace(i[0], str(i[1]))
                
                for i in psutil.disk_partitions():
                    tempValue = setTag(data[lang]["messages"]["disk"], message)
                    try:
                        usage = psutil.disk_usage(i.mountpoint)
                    except:
                        if setTag(data[lang]["error"]["PythonVersionError"], message) not in disk:
                            disk.append(setTag(data[lang]["error"]["PythonVersionError"], message))
                        continue
                    tempValue = tempValue.replace("[diskName]", i.device).replace("[diskUsage]", f"{usage.used / (1024 ** 3):.2f}")
                    tempValue = tempValue.replace("[diskMemory]", f"{usage.total / (1024 ** 3):.2f}").replace("[diskFree]", f"{usage.free / (1024 ** 3):.2f}")
                    disk.append(tempValue)
                messageText = messageText.replace("[disk]", "\n".join(disk))
                
                bot.edit_message_text(messageText,message.chat.id,message.id+1)

            case "scroll":
                if len(text.split()) != 2:
                    bot.send_message(chat.id,setTag(data[lang]["error"]["press"],message))
                else:
                    pag.scroll(int(text.split()[1]))

                    answerWithPic(message,data[lang]["messages"]["success"])

            case "say":
                if len(text.split()) < 3:
                    bot.send_message(chat.id,setTag(data[lang]["error"]["say"],message))
                elif len(text.split()[1]) != 2:
                    bot.send_message(chat.id,setTag(data[lang]["error"]["language"],message))
                else:
                    try:

                        bot.send_message(message.chat.id,setTag(data[lang]["system"]["loading"], message))

                        gTTS(text=" ".join(text.split()[2:]), lang=text.split()[1]).save(f"{data["settings"]["tempFolder"]}/voice.mp3")

                        pygame.mixer.init()
                        pygame.mixer.music.load(f"{data["settings"]["tempFolder"]}/voice.mp3") # Загружаем аудиофайл в pygame
                        bot.edit_message_text(setTag(data[lang]["messages"]["play"], message),message.chat.id,message.id+1)
                        pygame.mixer.music.play() # Включаем
                        while pygame.mixer.music.get_busy(): 
                                pygame.time.Clock().tick(10)
                        pygame.quit()
                        bot.edit_message_text(setTag(data[lang]["messages"]["success"], message),message.chat.id,message.id+1)
                    except ValueError:
                        bot.send_message(message.chat.id,setTag(data[lang]["error"]["languageNotFound"], message))

            case "help":
                bot.send_message(chat.id,"📝")

            case "web":
                if len(text.split()) != 2:
                    bot.send_message(chat.id,setTag(data[lang]["error"]["web"],message))
                else:
                    webbrowser.open(text.split()[1])

                    answerWithPic(message,data[lang]["messages"]["success"])

            case "translate":
                if len(text.split()) <= 2:
                    bot.send_message(chat.id,setTag(data[lang]["error"]["languageNotFound"],message))
                if len(text.split()[1]) != 2:
                     bot.send_message(chat.id,setTag(data[lang]["error"]["language"],message))
                else:
                    translator = Translator()
                    translated = translator.translate(" ".join(text.split()[2:]), dest=text.split()[1])

                    bot.send_message(chat.id,setTag(data[lang]["messages"]["translate"], message).replace("[text]"," ".join(text.split()[2:])).replace("[translate]",translated.text))

            case "find":

                def find_file(file, start = "C:\\"):
                    path = []
                    bot.send_message(chat.id, setTag(data[lang]["messages"]["findStart"], message).replace("[filesLen]","0"))
                    for root, dirs, files in os.walk(start):
                        for i in files:
                            if file in i:
                                path.append(os.path.join(root, i)) 
                                try:
                                    bot.edit_message_text(chat_id=chat.id,message_id=message.id+1,text=setTag(data[lang]["messages"]["findStart"], message).replace("[filesLen]", str(len(path))))
                                except:
                                    bot.send_message(chat.id, setTag(data[lang]["messages"]["findStart"], message).replace("[filesLen]", str(len(path))))
                    return path
                try:
                    file = text.split()[1].lower()
                except:
                    bot.send_message(chat.id, setTag(data[lang]["error"]["fileNotGived"], message))
                    return None
                
                path = find_file(file)
                bot.delete_message(chat.id, message.id+1)
                if len(path) == 1:
                    bot.send_message(chat.id, setTag(data[lang]["messages"]["find"], message).replace("[path]", path[0]))
                elif len(path) == 0:
                    bot.send_message(chat.id, setTag(data[lang]["messages"]["fileNotFound"], message))
                else:
                    if len(setTag(data[lang]["messages"]["findMany"].replace("[path]", "[/cod][n]•[cod]".join(path)), message)) <= 4000:
                        bot.send_message(chat.id, setTag(data[lang]["messages"]["findMany"].replace("[path]", "[/cod][n]• [cod]".join(path)).replace("[filesCount]", str(len(path))), message))
                    else:
                        localText = setTag(data[lang]["messages"]["filesSoMany"].replace("[path]", "[/cod][n]• [cod]".join([r.choice(path), r.choice(path), r.choice(path), r.choice(path), r.choice(path)])).replace("[filesCount]", str(len(path))), message)
                        if len(localText) <= 4000:
                            bot.send_message(chat.id, localText)
                        else:
                            bot.send_message(chat.id, setTag(data[lang]["messages"]["filesSoMany"].replace("[path]", "[/cod][n]• [cod]".join([r.choice(path), r.choice(path)])).replace("[filesCount]", str(len(path))), message))
            
            case "clearchat":
                bot.send_message(chat.id, setTag(data[lang]["messages"]["startCleanChat"], message))

                if message.id > 100:
                    bot.send_message(chat.id, setTag(data[lang]["messages"]["timeCleanChat"], message).replace("[cleantime]", str(round(message.id/3))))

                for i in range(message.id, 1, -1):
                    try:
                        bot.delete_message(chat.id,i)
                    except:
                        pass
                try:
                    bot.delete_message(chat.id, message.id+2)
                except:
                    pass
                try:
                    bot.edit_message_text(chat_id=chat.id, message_id=message.id+1, text=setTag(data[lang]["messages"]["finishCleanChat"], message))
                except:
                    pass
    
            case "off":
                bot.send_message(chat.id, setTag(data[lang]["messages"]["off"], message))
                tk.destroy()
            
            case "get":
                try:
                    file = text.split()[1].lower()
                except:
                    bot.send_message(chat.id, setTag(data[lang]["error"]["fileNotGived"], message))
                    return None
                try:
                    with open(file, 'rb') as document:
                        bot.send_document(chat.id,document)
                except FileNotFoundError:
                    bot.send_message(chat.id, setTag(data[lang]["error"]["fileNotFound"].replace("[file]",file), message))


            case "listdir": # изменить команду в  вебе с showdir на listdir
                try:
                    dir = text.split()[1].lower()
                except:
                    bot.send_message(chat.id, setTag(data[lang]["error"]["dirNotGived"], message))
                    return None
                try:
                    if len(os.listdir(dir)) == 0:
                        bot.send_message(chat.id, setTag(data[lang]["messages"]["dirIsEmpty"], message))
                    else:
                        listDir = "[/cod]\n— [cod]".join(os.listdir(dir))
                        
                        bot.send_message(chat.id, setTag(data[lang]["messages"]["showDir"].replace("[showDir]", listDir).replace("[dir]", dir), message))


                except FileNotFoundError:
                    bot.send_message(chat.id, setTag(data[lang]["error"]["dirNotFound"].replace("[dir]", dir), message))

            case "random":
                try:
                    rand = text.split()
                    rand.pop(0)
                    rand = list(map(int, rand))

                    if not rand:
                        bot.send_message(chat.id, setTag(data[lang]["messages"]["randomDefault"], None).replace("[rand]",str(r.randint(0,100))))
                    
                    elif len(rand) == 1:
                        bot.send_message(chat.id, setTag(data[lang]["messages"]["randomWithA"], None).replace("[rand]",str(r.randint(min(0,rand[0]),max(0,rand[0])))).replace("[A]",str(rand[0])+"¯\\_(ツ)_/¯"))

                    else:
                        if rand[0] == rand[1]:
                            bot.send_message(chat.id, setTag(data[lang]["messages"]["randomWithAB"], None).replace("[rand]",f"{rand[0]} ¯\\_(ツ)_/¯").replace("[A]",str(rand[0])).replace("[B]",str(rand[1])))
                        else:
                            bot.send_message(chat.id, setTag(data[lang]["messages"]["randomWithAB"], None).replace("[rand]",str(r.randint(min(rand[0],rand[1]),max(rand[0],rand[1])))).replace("[A]",str(min(rand[0],rand[1]))).replace("[B]",str(max(rand[0],rand[1]))))
                except ValueError:
                    bot.send_message(chat.id, setTag(data[lang]["error"]["numberRandomError"], None))

            case "colorphoto":
                cap = cv2.VideoCapture(0)

                if not cap.isOpened():
                    bot.send_message(chat.id,setTag(data[lang]["error"]["cameraClosed"],message))
                    return None

                if len(text.split()) < 2:
                    color = "#FFF"
                else:
                    color = text.split()[1]
                    if not ((len(color) == 7 or len(color) == 4) and color.count("#") == 1 and all(char in "0123456789ABCDEFabcdef" for char in color[1:])):
                        color = "#FFF"


                tempTk = Tk()
                tempTk["bg"] = color
                tempTk.title = "think fast!!!!"
                tempTk.attributes("-fullscreen", True)
                tempTk.attributes("-topmost", True)
                tempTk.update_idletasks()
                tempTk.update()


                ret, frame = cap.read()

                if not ret:
                    pass 
                    return
                
                cv2.imwrite(f"{data["settings"]["tempFolder"]}/photo.jpg",frame)
                cap.release()
                

                image = PIL.Image.open(f"{data["settings"]["tempFolder"]}/photo.jpg")
                bot.send_photo(chat.id,image,setTag(data[lang]["messages"]["photo"],message))
                tempTk.destroy()

            case _:
                useCommand = False
                writeInConsole(setTag(data[lang]["system"]["text"].replace("[text]", text),message))
            
        if useCommand:
            writeInConsole(setTag(data[lang]["system"]["command"].replace("[command]", text),message))
                
                    

    @bot.message_handler(content_types=["document", "photo", "voice", "video_note", "video"])
    def media(message):
        

        def save_file(id, name, messageNeeded):
            fileInfo = bot.get_file(id)
            downloadedFile = bot.download_file(fileInfo.file_path)
            with open(os.path.join(data["settings"]["tempFolder"], name), 'wb') as new_file:
                new_file.write(downloadedFile)

            if messageNeeded:
                bot.send_message(chat.id,setTag(data[lang]["messages"]["saveFile"], message).replace("[docName]",name))


        if not data["settings"]["botWorking"]:
            return None

        user = message.from_user
        text = message.caption
        chat = message.chat

        log(data[lang]["log"]["useStart"], message)
        mode2mes(bot, message)

        if not data["settings"]["users"]:
            bot.send_message(message.chat.id,setTag(data[lang]["messages"]["answerForNotUsers"],message))
            return None
        
        if not (os.path.exists(data["settings"]["tempFolder"]) and os.path.isdir(data["settings"]["tempFolder"])):
            os.mkdir(data["settings"]["tempFolder"])

        if str(user.id) not in data["settings"]["users"]:
            bot.send_message(message.chat.id,setTag(data[lang]["messages"]["answerForNotUsers"],message))
            return None
        
        if chat.type != "private" and not data["settings"]["groups"]:
            bot.send_message(message.chat.id,setTag(data[lang]["messages"]["groupDisable"],message))
            return None
        
        if text:
            if "convert" in text and message.content_type == "document":
                
                writeInConsole(setTag(data[lang]["system"]["command"].replace("[command]", text),message))
                
                if len(text.split()) < 2:
                    bot.send_message(chat.id,setTag(data[lang]["error"]["formatNotFound"],message))
                    return None
                fileId = message.document.file_id
                tempName = f"temp{message.document.file_name}"
                
                bot.send_message(chat.id,setTag(data[lang]["messages"]["convertStart"], message))
                log(data[lang]["log"]["useCommand"], message)

                save_file(fileId, tempName, False)

                formatFile = bot.get_file(fileId).file_path.split(".")[-1]
                neededFormat = text.split()[1]
                newName = ""

                
                if neededFormat == "png":
                    if formatFile == "jpg":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.png"
                        image = PIL.Image.open(os.path.join(data["settings"]["tempFolder"], tempName))
                        image.save(os.path.join(data["settings"]["tempFolder"], newName))
                    
                elif neededFormat == "jpg":
                    if formatFile == "png":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.jpg"
                        image = PIL.Image.open(os.path.join(data["settings"]["tempFolder"], tempName))
                        image = image.convert("RGB")
                        image.save(os.path.join(data["settings"]["tempFolder"], newName))
                    elif formatFile == "heif" or formatFile == "heic":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.jpg"
                        PIL.Image.open(os.path.join(data["settings"]["tempFolder"], tempName)).save(os.path.join(data["settings"]["tempFolder"], newName))

                elif neededFormat == "webm":
                    if formatFile == "gif":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.webm"
                        with VideoFileClip(os.path.join(data["settings"]["tempFolder"], tempName)) as clip:
                            clip.write_videofile(os.path.join(data["settings"]["tempFolder"], newName), codec="libvpx", audio=False)

                elif neededFormat == "gif":
                    if formatFile == "webm" or formatFile == "mp4":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.gif"
                        with VideoFileClip(os.path.join(data["settings"]["tempFolder"], tempName)) as clip:
                            clip.write_gif(os.path.join(data["settings"]["tempFolder"], newName), fps=20, program="ffmpeg", opt="palettegen")
                    elif formatFile == "mkv":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.gif"
                        with VideoFileClip(os.path.join(data["settings"]["tempFolder"], tempName)) as clip:
                            clip.write_gif(os.path.join(data["settings"]["tempFolder"], newName), fps=20, program="ffmpeg", opt="palettegen")

                elif neededFormat == "mp4":
                    if formatFile == "gif" or formatFile == "mkv":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.mp4"
                        with VideoFileClip(os.path.join(data["settings"]["tempFolder"], tempName)) as clip:
                            clip.write_videofile(os.path.join(data["settings"]["tempFolder"], newName), codec="libx264", audio=False)
                
                elif neededFormat == "docx":
                    if formatFile == "pdf":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.docx"
                        pdf = fitz.open(os.path.join(data["settings"]["tempFolder"], tempName))
                        with open(os.path.join(data["settings"]["tempFolder"], newName), "w", encoding="utf-8") as docx:
                            for page in pdf:
                                docx.write(page.get_text())
                                docx.write("\n")
                        pdf.close()

                elif neededFormat == "csv":
                    if formatFile == "xlsx":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.csv"
                        pd.read_excel(os.path.join(data["settings"]["tempFolder"], tempName)).to_csv(os.path.join(data["settings"]["tempFolder"], newName),index=False)
                
                elif neededFormat == "xlsx":
                    if formatFile == "csv":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.xlsx"
                        pd.read_csv(os.path.join(data["settings"]["tempFolder"], tempName)).to_excel(os.path.join(data["settings"]["tempFolder"], newName), index=False)
                    
                    if formatFile == "db":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.xlsx"
                        conn = sqlite3.connect(os.path.join(data["settings"]["tempFolder"], tempName))
                        query = "SELECT name FROM sqlite_master WHERE type='table';"
                        tables = pd.read_sql_query(query, conn)
                        with pd.ExcelWriter(os.path.join(data["settings"]["tempFolder"], newName), engine="openpyxl") as writer:
                            for table_name in tables["name"]:
                                df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
                                df.to_excel(writer, sheet_name=table_name, index=False)
                        conn.close()
                
                elif neededFormat == "mp3":
                    if formatFile == "mp4":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.mp3"
                        with VideoFileClip(os.path.join(data["settings"]["tempFolder"], tempName)) as clip:
                            clip.audio.write_audiofile(os.path.join(data["settings"]["tempFolder"], newName))
                elif neededFormat == "mkv":
                    if formatFile == "gif" or formatFile == "mp4":
                        newName = f"{'.'.join(message.document.file_name.split(".")[:-1])}.mkv"
                        with VideoFileClip(os.path.join(data["settings"]["tempFolder"], tempName)) as clip:
                            clip.write_videofile(os.path.join(data["settings"]["tempFolder"], newName), codec="libx264")

                if not newName:
                    bot.send_message(chat.id, setTag(data[lang]["error"]["formatNotUsed"], message))
                    try:
                        os.remove(os.path.join(data["settings"]["tempFolder"], tempName))
                    except Exception as e:
                        print(e)
                    return None
                

                try:
                    os.remove(os.path.join(data["settings"]["tempFolder"], tempName))
                except Exception as e:
                    print(e)
                try:
                    with open(os.path.join(data["settings"]["tempFolder"], newName), "rb") as file:
                        bot.send_document(chat.id,file,caption=setTag(data[lang]["messages"]["convert"],message).replace("[pastFormat]", formatFile).replace("[newFormat]", neededFormat).replace("[newName]", newName))
                except Exception as e:
                    if "Error code: 413" in str(e):
                        bot.send_message(chat.id, setTag(data[lang]["error"]["tooBigFile"], message).replace("[path]", os.path.join(data["settings"]["tempFolder"], newName)))


        elif data["settings"]["autoSave"] or text == "save":
            if message.content_type == "photo":
                fileId = message.photo[-1].file_id
                save_file(fileId, f"{message.id}.jpg", True)
            
            elif message.content_type == "document":
                fileId = message.document.file_id
                fileName = message.document.file_name
                save_file(fileId, fileName)

            elif message.content_type == "video":
                fileId = message.video.file_id
                save_file(fileId, f"{message.id}.mp4", True)

            elif message.content_type == "video_note":
                fileId = message.video_note.file_id
                save_file(fileId, f"{message.id}.mp4", True)

            elif message.content_type == "voice":
                fileId = message.voice.file_id
                save_file(fileId, f"{message.id}.ogg", True)

    @bot.message_handler()
    def others(message):
        print(message)

            
        

    bot.polling(non_stop=True)



# Функция переключения работы бота
def botStartStop():
    global data

    
    if not data["settings"]["token"] or data["settings"]["token"] == data[lang]["system"]["tokenExample"]:
        writeInConsole(data[lang]["system"]["tokenNotFound"])
        return None

    try:
        botThread.start() # !!! CGI при установке на 3.13 и более новых
    except RuntimeError:
        pass

    if not data["settings"]["botWorking"]:
        log(data[lang]["log"]["botStart"], None)
        startButton.config(text=data[lang]["system"]["quitTitle"],bg=darkGreen)
        token.config(state=DISABLED, fg=grey)
        users.config(state=DISABLED)
        if toggleUsers.cget("fg") != black:
            users.config(fg=grey)

        if data["settings"]["users"]:
            writeInConsole(data[lang]["system"]["botWasStarted"].replace("[users]",str(len(data["settings"]["users"]))))
        else:
            writeInConsole(data[lang]["system"]["botWasStarted"].replace("[users]","0"))
        
    else:
        log(data[lang]["log"]["botStop"], None)
        startButton.config(text=data[lang]["system"]["startTitle"],bg=black)
        token.config(state=NORMAL, fg=white)
        users.config(state=NORMAL)
        if toggleUsers.cget("fg") != black:
            users.config(fg=white)
        writeInConsole(data[lang]["system"]["botWasStopped"])
    data["settings"]["botWorking"] = not data["settings"]["botWorking"]



# Ведение логов, в случае, если это включено
def log(text, message):
    
    now = dt.now()

    replace = {
        "[date]": now.strftime("%d.%m.%Y"),
        "[time]": now.strftime("%H:%M:%S")
    }
    if message:
        replace.update({
            "[user]": message.from_user.username,
            "[id]": message.from_user.id,
            "[text]": message.text
        })

    for i in replace:
        text = text.replace(i,str(replace[i]))

    if not (os.path.exists(data["settings"]["tempFolder"]) and os.path.isdir(data["settings"]["tempFolder"])):
        os.mkdir(data["settings"]["tempFolder"])
    if data["settings"]["log"]:
        with open(f"{data["settings"]["tempFolder"]}/log.txt", "a",-1,"utf-8") as logfile:
            logfile.write(text+"\n")

def help():
    now = dt.now()
    if now.hour < 6 or now.hour > 18:
        webbrowser.open(f"{os.path.dirname(os.path.abspath(__file__))}/tl/{data["settings"]["language"]}/dark.html")
    else:
        webbrowser.open(f"{os.path.dirname(os.path.abspath(__file__))}/tl/{data["settings"]["language"]}/light.html")



# Создание виджетов
# Создание консоли
console = Text(tk,
               bg = darkBlue,
               fg = green,
               bd = 0,
               height = 16,
               width = 39,
               font = ("Dimkin", 17),
               wrap = WORD,
               selectbackground = green,
               selectforeground = darkBlue,
               insertbackground = darkBlue,
               spacing3 = 1,) 
console.tag_configure("padding", lmargin1=20, lmargin2=20)
console.place(x=353,y=12)

def disable_typing(event):
    return "break"
console.bind("<Key>",disable_typing)



# Создание окна с указанием токена бота
Frame(tk,
      width = 330,
      height = 2,
      bg = grey).place(x=12,y=23)
Label(tk,
      text = data[lang]["system"]["tokenTitle"],
      font = ("Dimkin", 14),
      fg = grey,
      bg = tk["bg"],
      ).place(x=36, y=8)

def toggleTokenFunc():
    if token.cget("show") == "*":
        token.config(show="")
        toggleToken.config(image = eye_close)
    else:
        token.config(show="*")
        toggleToken.config(image = eye_open)

toggleToken = Button(tk,
                     image = eye_open,
                     borderwidth = 0,
                     height = 12,
                     width = 20,
                     bg = tk["bg"],
                     activebackground = tk["bg"],
                     command = toggleTokenFunc)
toggleToken.place(x=296, y=17)

def inToken(event):
    if token.get() == data[lang]["system"]["tokenExample"]:
        token.delete(0, "end")
        token.config(fg = white)
def outToken(event):
    if not token.get():
        token.insert(0, data[lang]["system"]["tokenExample"])
        token.config(fg = grey)

token = Entry(tk,
              fg = white,
              bg = tk["bg"],
              justify = "left",
              font = ("Dimkin", 16),
              selectbackground = grey,
              selectforeground = black,
              width = 41,
              bd = 0,
              insertbackground = grey,
              disabledbackground = black,
              disabledforeground = grey,
              show = "*")
token.place(x=12, y=36)

if data["settings"]["token"]:
    token.insert(0, data["settings"]["token"])

if not data["settings"]["token"]:
    outToken(None)

if data["settings"]["botWorking"]:
    token.config(fg = grey)

token.bind('<FocusIn>', inToken)
token.bind('<FocusOut>', outToken)



# Создание окна с пользователями
Frame(tk,
      width = 330,
      height = 2,
      bg=grey).place(x=12,y=83)
Label(tk,
      text = data[lang]["system"]["usersTitle"],
      font = ("Dimkin", 14),
      fg = grey,
      bg = tk["bg"],
      ).place(x=36, y=68)

def inUsers(event):
    if users.get("1.0","end-1c") == data[lang]["system"]["usersExample"]:
        users.delete("1.0",END)
        if toggleUsers.cget("fg") != black:
            users.config(fg = white)
        
def outUsers(event):
    if not users.get("1.0","end-1c"):
        users.insert("1.0", data[lang]["system"]["usersExample"])
        if toggleUsers.cget("fg") != black:
            users.config(fg = grey)
    
users = Text(tk,
             font=("Dimkin",16),
             width=41,
             height=2,
             bd=0,
             bg=black,
             fg=black,
             selectbackground=grey,
             selectforeground=black,
             insertbackground=grey)
users.place(x=12, y=90)

if data["settings"]["users"]:
    users.insert("1.0", data["settings"]["users"])

users.bind('<FocusIn>', inUsers)
users.bind('<FocusOut>', outUsers)

def toggleUsersFunc():
    if toggleUsers.cget("fg") == black: # если выключен > включить
        if not data["settings"]["botWorking"]:
            if users.get("1.0","end-1c") == data[lang]["system"]["usersExample"]:
                users.config(fg=grey)
            else:
                users.config(fg=white)
        else:
            users.config(fg=grey)
        toggleUsers.config(image = eye_close)
        toggleUsers.config(fg = white)
    else: # если включен > выключен
        users.config(fg=black)
        toggleUsers.config(image = eye_open)
        toggleUsers.config(fg = black)

toggleUsers = Button(tk,
                     image = eye_open,
                     borderwidth = 0,
                     height = 12,
                     width = 20,
                     bg = tk["bg"],
                     fg = black,
                     activebackground = tk["bg"],
                     command = toggleUsersFunc)
toggleUsers.place(x=296, y=77)

if not data["settings"]["users"]:
    outUsers(None)



# Окно с настройками
Frame(tk,
      width = 330,
      height = 2,
      bg=grey).place(x=12,y=163)
Label(tk,
      text = data[lang]["system"]["settingsTitle"],
      font = ("Dimkin", 14),
      fg = grey,
      bg = tk["bg"],
      ).place(x=36, y=148)



# Виджет изменения настройки "скрывать данные под спойлером"
hideSpoiler = BooleanVar(value=data["settings"]["hide"])
hideCheckButton = Checkbutton(tk,
                              text=data[lang]["system"]["hideSpoiler"],
                              variable=hideSpoiler,
                              fg=grey,
                              bg=tk["bg"],
                              font=("Dimkin",16))
hideCheckButton.place(x=12,y=175)

# Переключение на 2 сообщения мод
twoMesMode = BooleanVar(value=data["settings"]["2mesMode"])
twoMesModeCheckButton = Checkbutton(tk,
                              text=data[lang]["system"]["2messagesMode"],
                              variable=twoMesMode,
                              fg=grey,
                              bg=tk["bg"],
                              font=("Dimkin",16))
twoMesModeCheckButton.place(x=12,y=215)

# Включение / выключение логов
logs = BooleanVar(value=data["settings"]["log"])
logsButton = Checkbutton(tk,
                              text=data[lang]["system"]["logs"],
                              variable=logs,
                              fg=grey,
                              bg=tk["bg"],
                              font=("Dimkin",16))
logsButton.place(x=12,y=255)

# Выбор списка
style = ttk.Style()
style.theme_use("default")
style.configure(
    "Custom.TCombobox",
    fieldbackground=white,
    background=white,
    foreground=black,
    selectbackground=white, 
    selectforeground=black,)

options = os.listdir("tl")
try:
    options.remove("none")
except:
    pass
language = ttk.Combobox(tk, 
                        values=options, 
                        state="readonly", 
                        width=5,
                        style="Custom.TCombobox"
                        )
language.set(lang)
language.place(x=12,y=305)
Label(tk,
      text = data[lang]["system"]["language"],
      font = ("Dimkin", 14),
      fg = grey,
      bg = tk["bg"],
      ).place(x=62,y=300)

# Автосейв файлов
autoSave = BooleanVar(value=data["settings"]["autoSave"])
autoSaveButton = Checkbutton(tk,
                              text=data[lang]["system"]["autoSave"],
                              variable=autoSave,
                              fg=grey,
                              bg=tk["bg"],
                              font=("Dimkin",16))
autoSaveButton.place(x=12,y=345)



# Кнопка запуска бота
def enterStart(event):
    startButton.config(fg=white)
def leaveStart(event):
    startButton.config(fg=grey)

startButton = Button(tk,
                     bg=black,
                     fg=grey,
                     font=("Dimkin",16),
                     text=data[lang]["system"]["startTitle"],
                     width=20,
                     bd=0,
                     activebackground=black,
                     activeforeground=green,
                     command=botStartStop)
startButton.place(x=12, y=424)

if data["settings"]["botWorking"]:
    startButton.config(text=data[lang]["system"]["quitTitle"],bg=darkGreen)

startButton.bind("<Enter>", enterStart)
startButton.bind("<Leave>", leaveStart)


# Кнопка помощи
def enterHelp(event):
    helpButton.config(fg=white)
def leaveHelp(event):
    helpButton.config(fg=grey)

helpButton = Button(tk,
                     bg=black,
                     fg=grey,
                     font=("Dimkin",16),
                     text=data[lang]["system"]["helpTitle"],
                     width=20,
                     bd=0,
                     activebackground=black,
                     activeforeground=green,
                     command=help)
helpButton.place(x=182, y=424)

helpButton.bind("<Enter>", enterHelp)
helpButton.bind("<Leave>", leaveHelp)


# Запуск программы
writeInConsole(data[lang]["system"]["logo"])
writeInConsole(data[lang]["system"]["consoleTitle"])

if tempValue.strip("--")[0] == "errorOpenData":
    writeInConsole(data[lang]["error"]["openData"].replace("[e]",tempValue.strip("--")[1]))

def saveSettings():
    global data, lang
    
    while True:
        data["settings"]["token"] = None if token.get() == data[lang]["system"]["tokenExample"] else token.get()
        data["settings"]["users"] = None if users.get("1.0","end-1c") == data[lang]["system"]["usersExample"] else users.get("1.0","end-1c").split("\n")
        data["settings"]["hide"] = hideSpoiler.get()
        data["settings"]["2mesMode"] = twoMesMode.get()
        data["settings"]["log"] = logs.get()
        data["settings"]["autoSave"] = autoSave.get()
        
        if data["settings"]["language"] != language.get():
            data["settings"]["language"] = language.get()
            lang = data["settings"]["language"]
            messagebox.showinfo(title="",message=data[lang]["system"]["forAccept"])
            log(data[lang]["log"]["setNewLanguage"], None)
            
            with open("data/settings","w",-1,"utf-8") as file:
                json.dump(data["settings"], file, indent=4)

            tk.destroy()

        with open("data/settings","w",-1,"utf-8") as file:
            json.dump(data["settings"], file, indent=4)
        t.sleep(1)

writeInConsole(data[lang]["system"]["programStart"])


saveThread = threading.Thread(target=saveSettings, daemon = True)
saveThread.start()

botThread = threading.Thread(target=botFunc, daemon = True)
if bot:
    botpolling = True
    botThread.start()
else:
    botpolling = False
threading.Thread(target=consoleWriteText,daemon=True).start()

log(data[lang]["log"]["appIsRunning"], None)
tk.mainloop()
log(data[lang]["log"]["appIsDisabled"], None)