from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, PEKKA_COLOR, MID_GRAY
from src.data.story import SCENES
from src.engine.pixel_art import generate_market_scene, generate_frank_sprite
from src.engine.animation import RainSystem
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class MarketScene(SceneBase):
    SCENE_ID = "ch06_market"

    def setup(self):
        data = SCENES[self.SCENE_ID]
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_8"]),
            (data["texts"][2], WHITE),
        ]
        self.background = generate_market_scene()
        self.rain = RainSystem(INTERNAL_WIDTH, INTERNAL_HEIGHT, intensity=40)

        sprite = generate_frank_sprite(FRANK_COLORS["frank_8"], scale=3)
        self.background.blit(sprite, (350, 230))
        pekka = generate_frank_sprite(PEKKA_COLOR, scale=3)
        self.background.blit(pekka, (390, 230))
        self.meet_frank("frank_8")

        from src.scenes.chapters.ch08_kruununhaka import KruununhakaScene
        from src.scenes.chapters.ch07_park import ParkScene
        from src.scenes.endings import LostScene

        self.choices = [
            (data["choices"][0], KruununhakaScene()),
            (data["choices"][1], ParkScene()),
            (data["choices"][2], LostScene("lost_drunk")),
        ]
