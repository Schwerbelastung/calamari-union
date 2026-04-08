from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_katajanokka_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class KatajanokkaScene(SceneBase):
    SCENE_ID = "ch07_katajanokka"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_17"]),
            (data["texts"][2], WHITE),
        ]
        self.background = generate_katajanokka_scene()

        sprite = generate_frank_sprite(FRANK_COLORS["frank_17"], scale=3)
        self.background.blit(sprite, (270, 170))
        self.meet_frank("frank_17")

        from src.scenes.chapters.ch09_esplanadi import EsplanadiScene
        from src.scenes.chapters.ch08_senate_square import SenateSquareScene
        from src.scenes.endings import LostScene

        self.choices = [
            (data["choices"][0], EsplanadiScene()),
            (data["choices"][1], SenateSquareScene()),
            (data["choices"][2], LostScene("lost_ferry")),
        ]
