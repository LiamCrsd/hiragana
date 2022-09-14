import random
from tkinter import *
import tkinter.font as font
import time
import codecs

texte = 0,0
couple = 0,0
temps = 5000
taille = 150
choix = "fr"

def RandomWord(lettres):
    res = ""
    taille = random.randint(3,6)
    for i in range(taille):
        res += random.choice(lettres)
    return res

def hiragana():
    global choix
    liste_fr = ["a","i","u","e","o","ka","ki","ku","ke","ko","sa","shi","su","se","so","ta","chi","tsu","te","to","na","ni","nu","ne","no","ha","hi","fu","he","ho","ma","mi","mu","me","mo","ra","ri","ru","re","ro","wa","wo","n","ga","gi","gu","ge","go","za","ji","zu","ze","zo","da","de","do","ba","bi","bu","be","bo","pa","pi","pu","pe","po"]
    liste_jap = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","ら","り","る","れ","ろ","わ","を","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ","ん"]
    if choix == "fr":
        def start():
            print("ok")
            label.config(text=random.choice(liste_fr))
            label['font'] = f
            label.pack()
            label.after(temps, start)
        fenetre = Tk()
        f = font.Font(size=600)
        label = Label(fenetre,text=random.choice(liste_fr))
        label['font'] = f
        label.pack()
        label.after(temps, start)
        fenetre.mainloop()
    else:
        def start():
            print("ok")
            label.config(text=RandomWord(liste_jap))
            label['font'] = f
            label.pack()
            label.after(temps, start)
        fenetre = Tk()
        f = font.Font(size=taille)
        label = Label(fenetre,text=RandomWord(liste_jap))
        label['font'] = f
        label.pack()
        label.after(temps, start)
        fenetre.mainloop()

def vocabulaire():
    liste_voc = []
    fichier = codecs.open("voc2.txt",mode="r",encoding="utf-8")
    lignes = fichier.readlines()
    for e in lignes:
        t = e.split(",")
        a,b = t[0].strip(),t[1].strip()
        liste_voc.append((a,b))
    print(liste_voc)
    global choix
    choice = choix
    global texte
    if choice == "jap":
        def next():
            global texte
            label.config(text=texte[1])
            label['font'] = f
            label.pack()
            label.after(temps,start)
        def start():
            global texte
            texte = random.choice(liste_voc)
            label.config(text=texte[0])
            label['font'] = f
            label.pack()
            label.after(7500, next)
        fenetre = Tk()
        f = font.Font(size=taille)
        texte = random.choice(liste_voc)
        label = Label(fenetre,text=texte[0])
        label['font'] = f
        label.pack()
        label.after(7500, next)
        fenetre.mainloop()
    elif choice == "fr":
        def next():
            print("ko")
            global texte
            label.config(text=texte[0])
            label['font'] = f
            label.pack()
            label.after(7500,start)
        def start():
            global texte
            texte = random.choice(liste_voc)
            label.config(text=texte[1])
            label['font'] = f
            label.pack()
            label.after(temps, next)
        fenetre = Tk()
        f = font.Font(size=taille)
        texte = random.choice(liste_voc)
        label = Label(fenetre,text=texte[1])
        label['font'] = f
        label.pack()
        label.after(temps, next)
        fenetre.mainloop()
    else:
        def next():
            global couple
            texte,num = couple
            num = 1 - num
            label.config(text=texte[num],fg = "green")
            label['font'] = f
            label.pack()
            label.after(int(temps/2),start)
        def start():
            global couple
            couple = random.choice(liste_voc),random.randint(0,1)
            label.config(text=couple[0][couple[1]],fg="black")
            label['font'] = f
            label.pack()
            label.after(temps, next)
        global couple
        couple = random.choice(liste_voc),random.randint(0,1)
        fenetre = Tk()
        f = font.Font(size=taille)
        label = Label(fenetre,text=couple[0][couple[1]])
        label['font'] = f
        label.pack()
        label.after(temps, next)
        fenetre.mainloop()

def nombre():
    temps *= 3
    liste_chiffre = ["","一","二","三","四","五","六","七","八","九"]
    liste_dix = ["","十","百","千","万"]
    def int_2_jap(n):
        res = ""
        n = str(n)
        compteur = 0
        for k in range(len(n)-1,-1,-1):
            res = liste_chiffre[int(n[k])] + liste_dix[compteur] + res
            compteur += 1
        return res
    global choix
    choice = choix
    if choice == "fr":
        def start():
            print("ok")
            label.config(text=str(random.randint(1000,100000)))
            label['font'] = f
            label.pack()
            label.after(5000, start)
        fenetre = Tk()
        f = font.Font(size=200)
        label = Label(fenetre,text=str(random.randint(1000,100000)))
        label['font'] = f
        label.pack()
        label.after(5000, start)
        fenetre.mainloop()
    else:
        def start():
            print("ok")
            label.config(text=int_2_jap(random.randint(1000,100000)))
            label['font'] = f
            label.pack()
            label.after(5000, start)
        fenetre = Tk()
        f = font.Font(size=200)
        label = Label(fenetre,text=int_2_jap(random.randint(1000,100000)))
        label['font'] = f
        label.pack()
        label.after(5000, start)
        fenetre.mainloop()
def switch():
    global choix
    if choix == "fr":
        choix = "jap"
    else:
        choix = "fr"
app = Tk()
f = font.Font(size=600)
label = Label(app,text="Choisir le mode").pack()
button1 = Button(app,text="hiragana",command=hiragana).pack()
button2 = Button(app,text="nombre",command=nombre).pack()
button3 = Button(app,text="vocabulaire",command=vocabulaire).pack()
button4 = Button(app,text="switch",command=switch).pack()
app.mainloop()
