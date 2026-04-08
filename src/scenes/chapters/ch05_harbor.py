from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_harbor_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class HarborScene(SceneBase):
    SCENE_ID = "ch05_harbor"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_16"]),
            (data["texts"][2], FRANK_COLORS["frank_16"]),
        ]
        self.background = generate_harbor_scene()

        sprite = generate_frank_sprite(FRANK_COLORS["frank_16"], scale=3)
        self.background.blit(sprite, (260, 160))
        self.meet_frank("frank_16")

        from src.scenes.chapters.ch07_katajanokka import KatajanokkaScene
        from src.scenes.chapters.ch05_cafe import CafeScene
        from src.scenes.endings import DeathScene

        self.choices = [
            (data["choices"][0], KatajanokkaScene()),
            (data["choices"][1], CafeScene()),
            (data["choices"][2], DeathScene("death_coast_guard")),
        ]
