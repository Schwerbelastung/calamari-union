from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_courtyard_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class CourtyardScene(SceneBase):
    SCENE_ID = "ch03_courtyard"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], WHITE),
        ]
        self.background = generate_courtyard_scene()

        from src.scenes.chapters.ch03_rooftop import RooftopScene
        from src.scenes.chapters.ch04_metro import MetroScene
        from src.scenes.endings import LostScene

        self._metro = MetroScene()

        self.choices = [
            (data["choices"][0], LostScene("lost_woman")),
            (data["choices"][1], RooftopScene()),
            (data["choices"][2], None),
        ]

    def on_choice(self, index):
        if index == 2 and len(self.choices) > 2:
            self.meet_frank("frank_5")
            self.text_blocks.append(
                (self.get_extra("frank_fence"), FRANK_COLORS["frank_5"])
            )
            self.current_block = len(self.text_blocks) - 1
            self.scene_manager.renderer.start_typewriter(
                self.text_blocks[-1][0], self.text_blocks[-1][1]
            )
            self.phase = "text"
            self.choices = [
                (self.get_extra("fence_choice"), self._metro),
            ]
        else:
            super().on_choice(index)
