from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.data.story import SCENES
from src.engine.pixel_art import generate_courtyard_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class CourtyardScene(SceneBase):
    SCENE_ID = "ch03_courtyard"

    def setup(self):
        data = SCENES[self.SCENE_ID]
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], WHITE),
        ]
        self.background = generate_courtyard_scene()

        from src.scenes.chapters.ch05_tunnels import TunnelScene
        from src.scenes.chapters.ch04_metro import MetroScene
        from src.scenes.endings import LostScene

        self._metro = MetroScene()

        self.choices = [
            (data["choices"][0], LostScene("lost_woman")),
            (data["choices"][1], TunnelScene()),
            (data["choices"][2], None),  # handled in on_choice
        ]

    def on_choice(self, index):
        if index == 2 and len(self.choices) > 2:
            self.meet_frank("frank_5")
            self.text_blocks.append(
                ("Frank waits in the shadows. Minutes pass. An hour. "
                 "Then another Frank appears, climbing over the fence "
                 "from the other side. He nods, as if this meeting was "
                 "prearranged, which it wasn't.",
                 FRANK_COLORS["frank_5"])
            )
            self.current_block = len(self.text_blocks) - 1
            self.scene_manager.renderer.start_typewriter(
                self.text_blocks[-1][0], self.text_blocks[-1][1]
            )
            self.phase = "text"
            self.choices = [
                ("Continue together toward the metro", self._metro),
            ]
        else:
            super().on_choice(index)
