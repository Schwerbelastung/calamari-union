from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.data.story import SCENES
from src.engine.pixel_art import generate_dumpster_alley_scene, generate_frank_sprite
from src.engine.animation import RainSystem
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class DumpsterAlleyScene(SceneBase):
    SCENE_ID = "ch02_dumpster"

    def setup(self):
        data = SCENES[self.SCENE_ID]
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_3"]),
            (data["texts"][2], FRANK_COLORS["frank_3"]),
        ]
        self.background = generate_dumpster_alley_scene()
        self.rain = RainSystem(INTERNAL_WIDTH, INTERNAL_HEIGHT, intensity=25)

        sprite = generate_frank_sprite(FRANK_COLORS["frank_3"], scale=3)
        self.background.blit(sprite, (360, 240))
        self.meet_frank("frank_3")

        from src.scenes.chapters.ch03_hameentie import HameentieScene

        self.choices = [
            (data["choices"][0], None),  # handled in on_choice
            (data["choices"][1], HameentieScene()),
        ]
        self._hameentie = HameentieScene()

    def on_choice(self, index):
        if index == 0 and not self.get_flag("has_map"):
            self.set_flag("has_map")
            self.text_blocks.append(
                ("Frank takes the map. It is damp and smells of coffee grounds. "
                 "Some of the streets are labeled. Some are not. "
                 "It is the most helpful thing that has happened all night.",
                 WHITE)
            )
            self.current_block = len(self.text_blocks) - 1
            self.scene_manager.renderer.start_typewriter(
                self.text_blocks[-1][0], self.text_blocks[-1][1]
            )
            self.phase = "text"
            self.choices = [
                ("Continue toward Hameentie", self._hameentie),
            ]
        else:
            super().on_choice(index)
