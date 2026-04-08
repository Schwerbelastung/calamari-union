from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_metro_train_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class MetroTrainScene(SceneBase):
    SCENE_ID = "ch04_metro_train"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_15"]),
            (data["texts"][2], FRANK_COLORS["frank_15"]),
        ]
        self.background = generate_metro_train_scene()

        sprite = generate_frank_sprite(FRANK_COLORS["frank_15"], scale=3)
        self.background.blit(sprite, (230, 200))
        self.meet_frank("frank_15")

        from src.scenes.chapters.ch05_harbor import HarborScene
        from src.scenes.chapters.ch05_tunnels import TunnelScene
        from src.scenes.endings import DeathScene

        self._harbor = HarborScene()

        self.choices = [
            (data["choices"][0], None),
            (data["choices"][1], DeathScene("death_metro_crash")),
            (data["choices"][2], TunnelScene()),
        ]

    def on_choice(self, index):
        if index == 0 and len(self.choices) > 1:
            self.text_blocks.append(
                (self.get_extra("let_drive_1"), MID_GRAY)
            )
            self.text_blocks.append(
                (self.get_extra("let_drive_2"), FRANK_COLORS["frank_15"])
            )
            self.current_block = len(self.text_blocks) - 2
            self.scene_manager.renderer.start_typewriter(
                self.text_blocks[self.current_block][0],
                self.text_blocks[self.current_block][1],
            )
            self.phase = "text"
            self.choices = [
                (self.get_extra("let_drive_choice"), self._harbor),
            ]
        else:
            super().on_choice(index)
