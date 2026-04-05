from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.data.story import SCENES
from src.engine.pixel_art import generate_hameentie_scene, generate_frank_sprite
from src.engine.animation import RainSystem
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class HameentieScene(SceneBase):
    SCENE_ID = "ch03_hameentie"

    def setup(self):
        data = SCENES[self.SCENE_ID]
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_4"]),
        ]
        self.background = generate_hameentie_scene()
        self.rain = RainSystem(INTERNAL_WIDTH, INTERNAL_HEIGHT, intensity=35)

        sprite = generate_frank_sprite(FRANK_COLORS["frank_4"], scale=3)
        self.background.blit(sprite, (300, 230))
        self.meet_frank("frank_4")

        from src.scenes.chapters.ch04_car import CarScene
        from src.scenes.chapters.ch04_metro import MetroScene
        from src.scenes.endings import DeathScene

        self.choices = [
            (data["choices"][0], CarScene()),
            (data["choices"][1], DeathScene("death_tram_tracks")),
            (data["choices"][2], MetroScene()),
        ]
