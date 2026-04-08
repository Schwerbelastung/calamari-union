from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_park_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class ParkScene(SceneBase):
    SCENE_ID = "ch07_park"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], MID_GRAY),
            (data["texts"][2], FRANK_COLORS["frank_9"]),
        ]
        self.background = generate_park_scene()

        sprite = generate_frank_sprite(FRANK_COLORS["frank_9"], scale=3)
        self.background.blit(sprite, (310, 260))
        self.meet_frank("frank_9")

        from src.scenes.chapters.ch09_esplanadi import EsplanadiScene
        from src.scenes.chapters.ch08_kruununhaka import KruununhakaScene
        from src.scenes.endings import LostScene

        self.choices = [
            (data["choices"][0], EsplanadiScene()),
            (data["choices"][1], KruununhakaScene()),
            (data["choices"][2], LostScene("lost_bench")),
        ]
