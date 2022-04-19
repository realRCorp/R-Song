import pygame
import math
from sound import SoundManager

current_path_file = ""

class Game:

    def __init__(self):
        pygame.init()

        self.is_playing = False
        self.notice = False
        self.end_game = False

        self.size_window = []
        with open(current_path_file+"data\settings.txt", "r", encoding="UTF-8") as t:
            n = 0
            for i in t:
                if n == 0 or n == 1:
                    self.size_window.append(int(i))
                n += 1
        if self.size_window[0] <= 0 or self.size_window[1] <= 0:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.size_window[0] = pygame.display.get_surface().get_width()
            self.size_window[1] = pygame.display.get_surface().get_height()
        else:
            self.screen = pygame.display.set_mode(self.size_window)

        icon = pygame.image.load('data/assets/logo.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption("R-Song")
        self.background = pygame.image.load(current_path_file+'data/assets/white.png')

        #banner
##        self.banner = pygame.image.load('assets/play_button.png')
##        self.banner = pygame.transform.scale(self.banner,(100,100))
##        self.banner_rect = self.banner.get_rect()
##        self.banner_rect.x = math.ceil(self.screen.get_width() / 3)
##        self.banner_rect.y = math.ceil(self.screen.get_height() / 2)
        #bouton

        self.play_button = pygame.image.load(current_path_file+'data/assets/play_button.png')
        self.play_button = pygame.transform.scale(self.play_button, (int(100/2000*self.size_window[0]), int(100/1000*self.size_window[1])))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = math.ceil(self.screen.get_width() / 3)
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 2)

        #i
        self.i = pygame.image.load(current_path_file+'data/assets/i.png')
        self.i = pygame.transform.scale(self.i, (int(50/2000*self.size_window[0]), int(50/1000*self.size_window[1])))
        self.i_rect = self.i.get_rect()
        self.i_rect.x = math.ceil(self.screen.get_width() - int(1.5*(50/2000*self.size_window[0])))
        self.i_rect.y = math.ceil(0 + int(50/1000*self.size_window[1]/2))


        #son
        self.sound_manager = SoundManager()
        #score
        self.score = 0
        self.music = 0
        #text
        self.font = pygame.font.SysFont("Oswald", 32)
        self.font2 = pygame.font.SysFont("Square Peg",64)
        self.font3 = pygame.font.SysFont("Square Peg", 32)
        self.str = ""
        self.letter_keyboard = None
        self.y = None


    def run(self):
        running = True
        while running:
            self.screen.blit(self.background, (0,0))




            if self.is_playing == True:
                self.update()
            elif self.notice == True:
                self.notice_1()
            elif self.end_game == True:
                self.game_end()
            else:
                self.screen.blit(self.play_button, self.play_button_rect)
                self.screen.blit(self.i, self.i_rect)

            self.guess = self.font2.render(self.str, 1, (0,0,0))
            self.screen.blit(self.guess, (int(50/2000*self.size_window[0]), int(900/1000*self.size_window[1])))
            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        self.start()
                    elif self.i_rect.collidepoint(event.pos):
                        self.notice = True
                    elif self.notice == True:
                        if self.echap_rect.collidepoint(event.pos):
                            self.notice = False
                    elif self.end_game == True:
                        if self.echap_rect.collidepoint(event.pos):
                            self.end_game = False
                            self.game_over()
                    elif self.is_playing == True:
                        if self.banner_rect.collidepoint(event.pos):
                            self.sound_manager.pause()
                        elif self.play_button_rect2.collidepoint(event.pos):
                            self.next()
                        elif self.echap_rect.collidepoint(event.pos):
                            self.exit()
                        elif self.play_button_rect3.collidepoint(event.pos):
                            self.sound_manager.unpause()
                        elif self.cancel_rect.collidepoint(event.pos):
                            pygame.mixer.music.rewind()
                        elif self.enter_rect.collidepoint(event.pos):
                            self.victory(self.str, self.y)
                        elif self.end_rect.collidepoint(event.pos):
                            self.sound_manager.stop()
                            self.end_game = True
                            self.is_playing = False




                elif event.type == pygame.KEYDOWN:
                    if self.is_playing == True:
                    # take the input of the letters of the player's keyboard
                        if event.key == pygame.K_q: self.letter_keyboard = "A"
                        elif event.key == pygame.K_b: self.letter_keyboard = "B"
                        elif event.key == pygame.K_c: self.letter_keyboard = "C"
                        elif event.key == pygame.K_d: self.letter_keyboard = "D"
                        elif event.key == pygame.K_e: self.letter_keyboard = "E"
                        elif event.key == pygame.K_f: self.letter_keyboard = "F"
                        elif event.key == pygame.K_g: self.letter_keyboard = "G"
                        elif event.key == pygame.K_h: self.letter_keyboard = "H"
                        elif event.key == pygame.K_i: self.letter_keyboard = "I"
                        elif event.key == pygame.K_j: self.letter_keyboard = "J"
                        elif event.key == pygame.K_k: self.letter_keyboard = "K"
                        elif event.key == pygame.K_l: self.letter_keyboard = "L"
                        elif event.key == pygame.K_SEMICOLON: self.letter_keyboard = "M"
                        elif event.key == pygame.K_n: self.letter_keyboard = "N"
                        elif event.key == pygame.K_o: self.letter_keyboard = "O"
                        elif event.key == pygame.K_p: self.letter_keyboard = "P"
                        elif event.key == pygame.K_a: self.letter_keyboard = "Q"
                        elif event.key == pygame.K_r: self.letter_keyboard = "R"
                        elif event.key == pygame.K_s: self.letter_keyboard = "S"
                        elif event.key == pygame.K_t: self.letter_keyboard = "T"
                        elif event.key == pygame.K_u: self.letter_keyboard = "U"
                        elif event.key == pygame.K_v: self.letter_keyboard = "V"
                        elif event.key == pygame.K_z: self.letter_keyboard = "W"
                        elif event.key == pygame.K_x: self.letter_keyboard = "X"
                        elif event.key == pygame.K_y: self.letter_keyboard = "Y"
                        elif event.key == pygame.K_w: self.letter_keyboard = "Z"
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: self.victory(self.str, self.y)
                        elif event.key == 8: self.letter_keyboard = "delete"
                        elif event.key == pygame.K_LEFT: self.letter_keyboard = "left"
                        elif event.key == pygame.K_RIGHT: self.letter_keyboard = "right"
                        elif event.key == pygame.K_SPACE: self.letter_keyboard = " "
                        elif event.key == pygame.K_ESCAPE: self.exit()
                        elif event.key == pygame.K_KP0 or event.key == pygame.K_0: self.letter_keyboard = "0"
                        elif event.key == pygame.K_KP1 or event.key == pygame.K_1: self.letter_keyboard = "1"
                        elif event.key == pygame.K_KP2 or event.key == pygame.K_2: self.letter_keyboard = "2"
                        elif event.key == pygame.K_KP3 or event.key == pygame.K_3: self.letter_keyboard = "3"
                        elif event.key == pygame.K_KP4: self.letter_keyboard = "4"
                        elif event.key == pygame.K_KP5 or event.key == pygame.K_5: self.letter_keyboard = "5"
                        elif event.key == pygame.K_KP6 or event.key == pygame.K_6: self.letter_keyboard = "6"
                        elif event.key == pygame.K_KP7 or event.key == pygame.K_7: self.letter_keyboard = "7"
                        elif event.key == pygame.K_KP8 or event.key == pygame.K_8: self.letter_keyboard = "8"
                        elif event.key == pygame.K_KP9 or event.key == pygame.K_9: self.letter_keyboard = "9"
                        elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS: self.letter_keyboard = "-"
                        elif event.key == pygame.K_4: self.letter_keyboard = "'"
                    else:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: self.start()
            if self.letter_keyboard != None:
                if self.letter_keyboard != "right" and self.letter_keyboard != "left":
                    if self.letter_keyboard == "delete":
                        if len(self.str)<1:
                            pass
                        else:
                            self.str_fast = ""
                            for i in range(len(self.str)-1):
                                self.str_fast += self.str[i]
                            self.str = self.str_fast
                            self.letter_keyboard = None
                    else:
                        self.str += self.letter_keyboard
                        self.letter_keyboard = None

    def game_over(self):
        self.is_playing = False
        self.score = 0
        self.music = 0

    def next(self):
        self.verif = 0
        for i in range(len(self.sound_manager.Check)):
            if not self.sound_manager.Check[i]:
                self.verif += 1
        if self.verif == 0:
            self.sound_manager.stop()
            self.end_game = True
            self.is_playing = False
            self.sound_manager.Check = [False for i in range(len(self.sound_manager.samples))]

        else:
            self.music +=1
            self.y = self.sound_manager.load()
            self.sound_manager.play()

    def exit(self):
        self.sound_manager.stop()
        self.game_over()

    def game_end(self):

        #end_panel
        self.end_panel = pygame.image.load(current_path_file+'data/assets/end_panel.png')
        self.end_panel = pygame.transform.scale(self.end_panel, (int(800/2000*self.size_window[0]), int(600/1000*self.size_window[1])))
        self.end_panel_rect = self.end_panel.get_rect()
        self.end_panel_rect.x = int(600/2000*self.size_window[0])
        self.end_panel_rect.y = int(200/1000*self.size_window[1])
        self.screen.blit(self.end_panel, self.end_panel_rect)

        #echap
        self.echap = pygame.image.load(current_path_file+'data/assets/echap.png')
        self.echap = pygame.transform.scale(self.echap, (int(50/2000*self.size_window[0]), int(50/1000*self.size_window[1])))
        self.echap_rect = self.echap.get_rect()
        self.echap_rect.x = int(620/2000*self.size_window[0])
        self.echap_rect.y = int(220/1000*self.size_window[1])
        self.screen.blit(self.echap, self.echap_rect)

        #score_final
        self.score_text_final = self.font3.render("Votre score final est de {} sur {}.".format(self.score, self.music-1), 1, (0,0,0))
        self.screen.blit(self.score_text_final, (int(825/2000*self.size_window[0]), int(500/1000*self.size_window[1])))

    def notice_1(self):
        self.i2 = pygame.image.load(current_path_file+'data/assets/notice.png')
        self.i2 = pygame.transform.scale(self.i2, (int(666/2000*self.size_window[0]), int(900/1000*self.size_window[1])))
        self.i_rect2 = self.i2.get_rect()
        self.i_rect2.x = int(666/2000*self.size_window[0])
        self.i_rect2.y = int(50/1000*self.size_window[1])
        self.screen.blit(self.i2, self.i_rect2)

        #echap
        self.echap = pygame.image.load(current_path_file+'data/assets/echap.png')
        self.echap = pygame.transform.scale(self.echap,(int(50/2000*self.size_window[0]), int(50/1000*self.size_window[1])))
        self.echap_rect = self.echap.get_rect()
        self.echap_rect.x = int(686/2000*self.size_window[0])
        self.echap_rect.y = int(70/1000*self.size_window[1])
        self.screen.blit(self.echap, self.echap_rect)

    def update(self):

        self.score_text = self.font.render("Score : {}".format(self.score), 1, (0,0,0))
        self.screen.blit(self.score_text, (int(1500/2000*self.size_window[0]), int(20/1000*self.size_window[1])))
        self.music_text = self.font.render("Musique n° : {}".format(self.music), 1, (0,0,0))
        self.screen.blit(self.music_text, (int(1500/2000*self.size_window[0]), int(70/1000*self.size_window[1])))

        #banner
        self.banner = pygame.image.load(current_path_file+'data/assets/stop_button.png')
        self.banner = pygame.transform.scale(self.banner, (int(100/2000*self.size_window[0]), int(100/1000*self.size_window[1])))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = math.ceil(self.screen.get_width() / 5)
        self.banner_rect.y = math.ceil(self.screen.get_height() / 2)
        self.screen.blit(self.banner, self.banner_rect)

        #button2
        self.play_button2 = pygame.image.load(current_path_file+'data/assets/play_button_2.png')
        self.play_button2 = pygame.transform.scale(self.play_button2, (int(100/2000*self.size_window[0]), int(100/1000*self.size_window[1])))
        self.play_button_rect2 = self.play_button2.get_rect()
        self.play_button_rect2.x = math.ceil(self.screen.get_width() / 10)
        self.play_button_rect2.y = math.ceil(self.screen.get_height() / 2)
        self.screen.blit(self.play_button2, self.play_button_rect2)

        #echap
        self.echap = pygame.image.load(current_path_file+'data/assets/echap.png')
        self.echap = pygame.transform.scale(self.echap, (int(50/2000*self.size_window[0]), int(50/1000*self.size_window[1])))
        self.echap_rect = self.echap.get_rect()
        self.echap_rect.x = int(20/2000*self.size_window[0])
        self.echap_rect.y = int(20/1000*self.size_window[1])
        self.screen.blit(self.echap, self.echap_rect)

        #unpause
        self.play_button3 = pygame.image.load(current_path_file+'data/assets/play_button_3.png')
        self.play_button3 = pygame.transform.scale(self.play_button3, (int(100/2000*self.size_window[0]), int(100/1000*self.size_window[1])))
        self.play_button_rect3 = self.play_button3.get_rect()
        self.play_button_rect3.x = math.ceil(self.screen.get_width() / 3.33)
        self.play_button_rect3.y = math.ceil(self.screen.get_height() / 2)
        self.screen.blit(self.play_button3, self.play_button_rect3)

        #cancel_button
        self.cancel = pygame.image.load(current_path_file+'data/assets/cancel_button.png')
        self.cancel = pygame.transform.scale(self.cancel, (int(100/2000*self.size_window[0]), int(100/1000*self.size_window[1])))
        self.cancel_rect = self.cancel.get_rect()
        self.cancel_rect.x = math.ceil(self.screen.get_width() / 2.5)
        self.cancel_rect.y = math.ceil(self.screen.get_height() / 2)
        self.screen.blit(self.cancel, self.cancel_rect)

        #enter
        self.enter = pygame.image.load(current_path_file+'data/assets/enter.png')
        self.enter = pygame.transform.scale(self.enter, (int(100/2000*self.size_window[0]), int(100/1000*self.size_window[1])))
        self.enter_rect = self.enter.get_rect()
        self.enter_rect.x = int(1350/2000*self.size_window[0])
        self.enter_rect.y = int(850/1000*self.size_window[1])
        self.screen.blit(self.enter, self.enter_rect)

        #end
        self.end = pygame.image.load(current_path_file+'data/assets/end.png')
        self.end = pygame.transform.scale(self.end, (int(200/2000*self.size_window[0]), int(150/1000*self.size_window[1])))
        self.end_rect = self.end.get_rect()
        self.end_rect.x = int(450/2000*self.size_window[0])
        self.end_rect.y = int(700/1000*self.size_window[1])
        self.screen.blit(self.end, self.end_rect)

    def victory(self, text, dict):
        if dict == None:
            self.str = ""
        else:
            if text == dict['titre'].upper() or text == dict['artiste'].upper():
                self.score += 1
                self.next()
                self.str = ""
            else:
                self.str = ""

    def start(self):
        self.is_playing = True
        self.next()



