from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.data.story import SCENES
from src.engine.pixel_art import generate_alley_scene, generate_frank_sprite
from src.engine.animation import RainSystem
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class AlleyScene(SceneBase):
    SCENE_ID = "ch02_alley"

    def setup(self):
        data = SCENES[self.SCENE_ID]
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_2"]),
            (data["texts"][2], FRANK_COLORS["frank_2"]),
        ]
        self.background = generate_alley_scene()
        self.rain = RainSystem(INTERNAL_WIDTH, INTERNAL_HEIGHT, intensity=30)

        # Frank #2 hiding behind bins
        sprite = generate_frank_sprite(FRANK_COLORS["frank_2"], scale=3)
        self.background.blit(sprite, (210, 240))
        self.meet_frank("frank_2")

        from src.scenes.chapters.ch03_hameentie import HameentieScene
        from src.scenes.chapters.ch03_courtyard import CourtyardScene
        from src.scenes.endings import DeathScene

        self.choices = [
            (data["choices"][0], HameentieScene()),
            (data["choices"][1], CourtyardScene()),
            (data["choices"][2], DeathScene("death_bar_return")),
        ]
