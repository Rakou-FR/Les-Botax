from PIL import Image, ImageDraw, ImageGrab, ImageFile
import pyautogui
import keyboard
import time
import random
import cv2

captcha_vert_r, captcha_vert_g, captcha_vert_b, captcha_vert_T = 16, 23, 41, 255 # en haut a gauche le premier pixel vert du captcha

liste_compte = []

def screen():
    capture = pyautogui.screenshot()
    capture.save(r"C:\Users\balin\OneDrive\Bureau\bot GouzouGouzou\capture.png")

def captcha_resolver():
    macro = True
    while macro == True:
        cours = True
        if keyboard.is_pressed("ctrl+!"):
            screen()
            while cours == True:
                vert_r, vert_g, vert_b = img.getpixel((827,421))
                if vert_r == captcha_vert_r and vert_g == captcha_vert_g and vert_b == captcha_vert_b:
                    for x in range(827,1086):
                        for y in range(421,504):
                            trouver_gris_r, trouver_gris_g, trouver_gris_b, trouver_gris_T = img.getpixel((x,y))
            coo = pyautogui.locateCenterOnScreen("bouton_vert.png")
            print(coo)
            pyautogui.click(coo)
        elif keyboard.is_pressed("²"):
            macro=False
        else:
            continue

def couleur(a,b):
    img = Image.open("capture.PNG")
    nr,nv,nb,nn = img.getpixel((a,b))
    print(nr,nv,nb,nn)

class running:
    def verif_bloquage():
        oui = 0
    def sus(nombre):
        print("program statut : running \nfollowing")
        macro = True
        bouclee = 0
        sortir = False
        coo_sabonner_temp = 0
        while macro == True:
            cours = True
            if keyboard.is_pressed("!"):
                boucle = 0
                while boucle < nombre:
                    coo_sabonner = pyautogui.locateCenterOnScreen("sabonner.png", confidence = 0.9)
                    bloquage = pyautogui.locateCenterOnScreen("bloquage.png")
                    if bloquage is not None:
                        print("bloquage")
                        ok = pyautogui.locateCenterOnScreen("OK.png")
                        pyautogui.click(ok)
                        time.sleep(2)
                        coo_croix = pyautogui.locateCenterOnScreen("croix.png")
                        pyautogui.click(coo_croix)
                        print("program statut : Stoped")
                        sortir = True
                        break
                    elif coo_sabonner is not None:
                        if coo_sabonner_temp == coo_sabonner:
                            pyautogui.click(coo_sabonner)
                            print("attendre : 2s")
                            time.sleep(2)
                        else:
                            time.sleep(1)
                            coo_sabonner_temp = coo_sabonner
                            pyautogui.click(coo_sabonner)
                            print("sabonner : ",boucle+1)
                            boucle += 1
                    elif boucle == nombre:
                        sortir = True
                        coo_croix = pyautogui.locateCenterOnScreen("croix.PNG")
                        if coo_croix is not None:
                            pyautogui.click(coo_croix)
                            print("croix")
                            break
                        else:
                            break
                    else:
                        print("descendre")
                        pyautogui.scroll(-200)
                        time.sleep(2)
            if sortir == True:
                break
            elif keyboard.is_pressed("p"):
                macro=False
            else:
                continue

    def desus(nombre):
        print("program statut : running \ndesus")
        macro = True
        bouclee = 0
        boucle = 0
        sortir = False
        coo_desabonner_temp = 0
        while macro == True:
            cours = True
            if keyboard.is_pressed("!"):
                while True:
                    bloquage = pyautogui.locateCenterOnScreen("bloquage.png", confidence = 0.9)
                    coo_desabonner = pyautogui.locateCenterOnScreen("desabonner.png", confidence = 0.9)
                    if bloquage is not None:
                        print("bloquage")
                        ok = pyautogui.locateCenterOnScreen("OK.png")
                        pyautogui.click(ok)
                        time.sleep(1)
                        coo_croix = pyautogui.locateCenterOnScreen("croix.png")
                        pyautogui.click(coo_croix)
                        print("program statut : Stoped")
                        sortir = True
                        break
                    elif coo_desabonner is not None:
                        if coo_desabonner_temp == coo_desabonner:
                            print("attendre : 15s")
                            time.sleep(15)
                        else:
                            while boucle < nombre:
                                print("desabonner : ",boucle+1)
                                boucle += 1
                                bouclee = boucle
                                coo_desabonner = pyautogui.locateCenterOnScreen("desabonner.png", confidence = 0.9)
                                if coo_desabonner is not None:
                                    pyautogui.click(coo_desabonner)
                                    coo_sedesabonner = pyautogui.locateCenterOnScreen("sedesabonner.png", confidence = 0.9)
                                    if coo_sedesabonner is not None:
                                        pyautogui.click(coo_sedesabonner)
                                        time.sleep(1)
                                    else:
                                        time.sleep(1)
                                else:
                                    pyautogui.scroll(-100)
                                    time.sleep(2)
                    elif bouclee == nombre:
                        sortir = True
                        print("croix")
                        coo_croix = pyautogui.locateCenterOnScreen("croix.png")
                        if coo_croix is not None:
                            pyautogui.click(coo_croix)
                            sortir = True
                            break
                    else:
                        continue
                if sortir == True:
                    break
            elif keyboard.is_pressed("p"):
                macro=False
            else:
                continue
running.sus(250)
