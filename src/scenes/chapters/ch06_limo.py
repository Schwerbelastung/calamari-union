from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_limo_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class LimoScene(SceneBase):
    SCENE_ID = "ch06_limo"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], MID_GRAY),
            (data["texts"][2], FRANK_COLORS["frank_13"]),
        ]
        self.background = generate_limo_scene()
        self.meet_frank("frank_13")

        from src.scenes.chapters.ch08_senate_square import SenateSquareScene
        from src.scenes.chapters.ch08_kruununhaka import KruununhakaScene
        from src.scenes.endings import DeathScene

        self.choices = [
            (data["choices"][0], SenateSquareScene()),
            (data["choices"][1], KruununhakaScene()),
            (data["choices"][2], DeathScene("death_limo_police")),
        ]
