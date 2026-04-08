from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_car_scene
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class CarScene(SceneBase):
    SCENE_ID = "ch04_car"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], MID_GRAY),
            (data["texts"][2], WHITE),
        ]
        self.background = generate_car_scene()

        from src.scenes.chapters.ch06_market import MarketScene
        from src.scenes.endings import DeathScene

        self.choices = [
            (data["choices"][0], MarketScene()),
            (data["choices"][1], DeathScene("death_car_fix")),
        ]
