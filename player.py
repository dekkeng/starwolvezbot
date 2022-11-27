import os, pyautogui
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
from random import uniform

load_dotenv("config.txt")

class Player:
    def __init__(self):
        self.CONFIDENCE = 0.9
        self.RANDOM_CLICK_SIZE = 10
        self.updatePos()

    def updatePos(self):
        self.ap = self.getPos("ap5", 0.9)
        self.cont = self.getPos("continue", self.CONFIDENCE)
        self.heal1 = self.getPos("heal1", self.CONFIDENCE)
        self.heavy1 = self.getPos("heavy1", self.CONFIDENCE)
        self.launch = self.getPos("launch", self.CONFIDENCE)
        self.pve = self.getPos("pve", self.CONFIDENCE)
        self.restore1 = self.getPos("restore1", self.CONFIDENCE)
        self.gohome = self.getPos("return", self.CONFIDENCE)
    
    def play(self):
        self.log("Play")
        is_heal = True
        while True:
            self.updatePos()
            if self.gohome != None:
                self.click(self.gohome)
                self.wait(3)
                break
            elif self.cont != None:
                self.click(self.cont)
                self.wait(1)
            elif self.ap != None:
                self.heal()
                if self.heavy1 != None:
                    for _ in range(10):
                        self.click(self.heavy1)
                        self.wait(0.1)
            else:
                if is_heal:
                    self.restore()
                    is_heal = False
                elif self.heal1 != None:
                    self.heal()
                    is_heal = True
            
            self.wait(0.1)

    def restore(self):
        if self.restore1 != None:
            self.click(self.restore1)
    def heal(self):
        if self.heal1 != None:
            self.click(self.heal1)

    def start(self):
        self.log("Start")
        while True:
            self.updatePos()
            if self.pve != None:
                self.click(self.pve)
                self.wait(5)
                self.play()
            elif self.launch != None:
                self.click(self.launch)
            elif self.restore1 != None:
                self.play()
            self.wait(0.3)

    def getPos(self, file, conf = 0.6):
        return pyautogui.locateCenterOnScreen('./sample/'+file+'.png', confidence = conf)

    def getAllPos(self, file, conf = 0.7):
        return pyautogui.locateAllOnScreen('./sample/'+file+'.png', confidence = conf)

    def wait(self, length = 0.01):
        sleep(uniform(length-0.01, length+0.01))

    def move(self, pos):
        pyautogui.moveTo(pos)
        
    def click(self, pos):
        pyautogui.click([uniform(pos[0], pos[0]+self.RANDOM_CLICK_SIZE), uniform(pos[1], pos[1]+self.RANDOM_CLICK_SIZE)])
        
    def log(self, msg):
        """Msg log"""
        t = datetime.now().strftime('%H:%M:%S')
        print(f'[{t}] MESSAGE: {msg}')
