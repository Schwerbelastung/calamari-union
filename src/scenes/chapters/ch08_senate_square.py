from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, MID_GRAY
from src.engine.pixel_art import generate_senate_square_scene
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class SenateSquareScene(SceneBase):
    SCENE_ID = "ch08_senate_square"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], MID_GRAY),
            (data["texts"][2], WHITE),
        ]
        self.background = generate_senate_square_scene()

        from src.scenes.chapters.ch09_esplanadi import EsplanadiScene
        from src.scenes.chapters.ch07_katajanokka import KatajanokkaScene
        from src.scenes.endings import DeathScene

        self.choices = [
            (data["choices"][0], EsplanadiScene()),
            (data["choices"][1], KatajanokkaScene()),
            (data["choices"][2], DeathScene("death_senate_patrol")),
        ]
