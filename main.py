from pygame import init as PyGameInit
from game_utils import GameStateManager, IoManager, SoundManager, UiManager


class Minesweeper:
    def __init__(self) -> None:
        PyGameInit()

        self.game_state_manager: GameStateManager = GameStateManager()
        self.sound_manager: SoundManager = SoundManager()
        self.ui_manager: UiManager = UiManager()
        self.io_manager: IoManager = IoManager()

    def play(self):
        self.screen.fill((60, 80, 100))

        while self.game_state_manager.running:

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

                if event.type == pygame.MOUSEMOTION:
                    self.mouse_coordinates = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()


game = Minesweeper()
game.play()
