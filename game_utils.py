from enum import Enum
from os.path import exists
from pygame import Surface, QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, mouse
from pygame._common import _Coordinate
from pygame.font import Font, SysFont
from pygame.display import Info, set_mode, update
from pygame.mixer import init as py_mixer, music
from pygame.mouse import get_pos
from pygame.event import get as get_event, Event


class GameStateManager:
    class GameState(Enum):

        MAIN_MENU = "MAIN MENU"
        PAUSED = "PAUSED"
        LOADING = "LOADING"
        PLAYING = "PLAYING"

    def __init__(self) -> None:
        self.game_state: GameStateManager.GameState = (
            GameStateManager.GameState.MAIN_MENU
        )
        self.running: bool = True

    def start_game(self):
        self.game_state = GameStateManager.GameState.PLAYING

    def pause_game(self):
        self.game_state = GameStateManager.GameState.PAUSED

    def unpause_game(self):
        self.game_state = GameStateManager.GameState.PLAYING

    def abandon_game(self):
        self.game_state = GameStateManager.GameState.MAIN_MENU

    def exit_game(self):
        self.game_state = GameStateManager.GameState.MAIN_MENU
        self.running = False

    


class SoundManager:
    def __init__(self) -> None:
        py_mixer()
        music.load("assets/rituel.mp3")
        music.play()

    def pause(self) -> None:
        music.pause()

    def unpause(self) -> None:
        music.unpause()

    def stop(self) -> None:
        music.stop()

    def play(self, path_to_music_file: str) -> None:
        if exists(path_to_music_file):
            music.load(path_to_music_file)
            music.play(loops=0)
        else:
            pass


class UiManager:
    def __init__(self) -> None:
        self._display_info = Info()
        self._screen_height = self.display_info.current_h
        self._screen_width = self.display_info.current_w
        self._font: Font = SysFont("arialblack", 40)
        self._screen: Surface = set_mode((self.screen_width, self.screen_height))

    def get_screen_dimensions(self):
        return self._screen_height, self._screen_width

    def get_base_canvas(self):
        return self._screen

    def get_base_font(self):
        return self._font

    def update_display(self):
        update()


class IoManager:
    def __init__(self) -> None:
        self.click: bool = False
        self.mouse_coordinates: _Coordinate

    def set_coordinates(self, x_coord: int, y_coord: int) -> None:
        self.mouse_coordinates = (x_coord, y_coord)

    def get_coordinates(self) -> _Coordinate:
        return self.mouse_coordinates

    def game_loop(self) -> bool:
        self.click = False
        for event in get_event():
            if event.type == QUIT:
                return False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

            if event.type == MOUSEMOTION:
                self.set_coordinates(mouse.get_pos())

        return True
