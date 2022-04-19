## Copyright Maranaï for RCorp™
import pygame
import csv
import random

current_path_file = ""

def csv__table(file_name):
        file = open(file_name,'r')
        table = list(csv.DictReader(file))
        file.close()
        return table

class SoundManager:
    def __init__(self):
        self.samples = csv__table(current_path_file+'data/liste_musiques.csv')
        self.Check = [False for i in range(len(self.samples))]

    def load(self):
        self.volume = 0.7
        with open(current_path_file+"data\settings.txt", "r", encoding="UTF-8") as t:
            n = 0
            for i in t:
                if n == 2:
                    if not float(i) <= 0:
                        self.volume = float(i)
                n += 1

        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.volume)
        nb = random.randint(0,len(self.samples)-1)


        while self.Check[nb]:
            nb = random.randint(0,len(self.samples)-1)
        self.Check[nb] = True
        pygame.mixer.music.load(current_path_file+'data/Samples/'+self.samples[nb]['sample'])
        return self.samples[nb]

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.quit()
        pygame.mixer.init()






##sound_manager = SoundManager()

