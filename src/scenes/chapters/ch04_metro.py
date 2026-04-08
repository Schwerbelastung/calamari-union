from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_metro_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class MetroScene(SceneBase):
    SCENE_ID = "ch04_metro"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_6"]),
            (data["texts"][2], FRANK_COLORS["frank_6"]),
        ]
        self.background = generate_metro_scene()

        sprite = generate_frank_sprite(FRANK_COLORS["frank_6"], scale=3)
        self.background.blit(sprite, (265, 268))
        self.meet_frank("frank_6")

        from src.scenes.chapters.ch05_tunnels import TunnelScene
        from src.scenes.chapters.ch04_metro_train import MetroTrainScene
        from src.scenes.chapters.ch06_market import MarketScene

        tunnel = TunnelScene()

        self.choices = [
            (data["choices"][0], None),
            (data["choices"][1], tunnel),
            (data["choices"][2], MetroTrainScene()),
            (data["choices"][3], MarketScene()),
        ]
        self._tunnel = tunnel

    def on_choice(self, index):
        if index == 0 and len(self.choices) > 1:
            self.text_blocks.append(
                (self.get_extra("wait_text"), MID_GRAY)
            )
            self.current_block = len(self.text_blocks) - 1
            self.scene_manager.renderer.start_typewriter(
                self.text_blocks[-1][0], self.text_blocks[-1][1]
            )
            self.phase = "text"
            self.choices = [
                (self.get_extra("wait_choice"), self._tunnel),
            ]
        else:
            super().on_choice(index)
