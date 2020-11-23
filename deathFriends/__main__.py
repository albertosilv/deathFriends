from .game import Game

def loop():
    g = Game()
    option = g.show_start_screen()
    if option == 1:
        g.nick_screen()
    if option == 9:
        while True:
            g.new()
            g.run()
            g.show_go_screen()


if __name__ == '__main__':
    loop()