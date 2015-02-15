from Battlefield.Battlefield import *
from GameState import GameState
from Shop import Shop
from Shop.ShopState import ShopState
import UI.Buttons
import Game
import pygame

def launch_game():
    button_height = 50
    status_width = 100
    shop_state = ShopState([], button_height, 1)
    shopping_screen = pygame.display.set_mode((shop_state.window_width, shop_state.window_height))
    units = Shop.run(shopping_screen, shop_state)
    battlefield = Battlefield(Battlefield.build("Battlefield/2.txt"))
    game_state = GameState(battlefield, button_height, status_width, units)
    battle_screen = pygame.display.set_mode((game_state.get_window_width(), game_state.get_window_height()))
    Game.run(battle_screen, game_state)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Heroes Emblem")

    screen = pygame.display.set_mode(((32 * 16) + 100, (32 * 9) + 50))
    StartGame = UI.Buttons.Button("Start Game")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if StartGame.pressed(pos):
                    launch_game()

        StartGame.create_button(screen, (50, 80, 200), ((32 * 16) - 100)/2, ((32 * 9) - 50)/2, 200, 100, None, (135, 144, 15))
        pygame.display.update()


