import pygame
from src.data.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS, TITLE, BLACK, STATE_QUIT,
)
from src.engine.renderer import Renderer
from src.engine.input_handler import InputHandler
from src.engine.scene_manager import SceneManager
from src.engine.music import MusicManager


class Game:
    def __init__(self):
        # Pre-init mixer before pygame.init() to ensure correct format
        from src.engine.music import SAMPLE_RATE, CHANNELS, SAMPLE_WIDTH
        pygame.mixer.pre_init(frequency=SAMPLE_RATE, size=-SAMPLE_WIDTH * 8, channels=CHANNELS, buffer=2048)
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.window)
        self.input = InputHandler()
        self.music = MusicManager()
        self.music.init()
        self.scene_manager = SceneManager(self.renderer, self.music)
        self.running = True

    def run(self, initial_scene):
        self.scene_manager.set_scene(initial_scene, immediate=True)

        while self.running:
            dt = self.clock.tick(FPS)
            events = pygame.event.get()
            self.input.update(events)

            if self.input.quit_requested:
                self.running = False
                break

            if self.input.just_pressed(pygame.K_ESCAPE):
                self.running = False
                break

            self.scene_manager.update(dt, self.input)

            self.renderer.clear()
            self.scene_manager.draw()
            self.renderer.present()

        self.music.stop()
        pygame.quit()
