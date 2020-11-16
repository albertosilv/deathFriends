import pygame as pg
from os import path
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)

        image_folder = path.join(game_folder, 'sprints')
        text_folder = path.join(game_folder, 'fonts')

        self.backgroudMenu_img = pg.image.load(
            path.join(image_folder, BACKGROUNDMENU))
        self.titleFont = pg.font.Font(path.join(text_folder, TILEFONT), 45)
        self.fontMenu = pg.font.Font(path.join(text_folder, MENUFONT), 35)


    def new(self):
       pass

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
       pass

    def draw(self):
        self.screen.fill(BGCOLOR)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
    def show_start_screen(self):
         while(True):
            for e in pg.event.get():
                if(e.type == pg.QUIT):
                    self.quit()
            self.screen.blit(self.backgroudMenu_img, (0, 0))

            # Titulo do jogo
            self.textObjetc('death friends', self.titleFont, 5)

            # Botoes
            self.textObjetc('Iniciar jogo', self.fontMenu, 2.5)
            self.textObjetc('Configurações', self.fontMenu, 2)
            self.textObjetc('Sair', self.fontMenu, 1.7)

            mousePosition = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            if(400 < mousePosition[0] < 565 and 245 < mousePosition[1] < 275) and click[0] == 1:
                return 1
            if(370 < mousePosition[0] < 585 and 305 < mousePosition[1] < 330 and click[0] == 1):
                self.quit()
            if(450 < mousePosition[0] < 510 and 360 < mousePosition[1] < 385 and click[0] == 1):
                self.quit()

            self.clock.tick(FPS)
            pg.display.flip()

    def show_go_screen(self):
        pass
    def textObjetc(self, text, font, location):
        textSurf = font.render(text, True, WHITE)
        textReact = textSurf.get_rect()
        textReact.center = (int(WIDTH/2), int(HEIGHT/location))
        self.screen.blit(textSurf, textReact)