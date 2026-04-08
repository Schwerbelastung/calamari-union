from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, MID_GRAY
from src.engine.pixel_art import generate_rooftop_scene
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class RooftopScene(SceneBase):
    SCENE_ID = "ch03_rooftop"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], MID_GRAY),
            (data["texts"][2], WHITE),
        ]
        self.background = generate_rooftop_scene()

        from src.scenes.chapters.ch03_hameentie import HameentieScene
        from src.scenes.chapters.ch05_cafe import CafeScene
        from src.scenes.endings import DeathScene

        self.choices = [
            (data["choices"][0], HameentieScene()),
            (data["choices"][1], CafeScene()),
            (data["choices"][2], DeathScene("death_rooftop_fall")),
        ]
