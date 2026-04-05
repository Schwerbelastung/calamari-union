from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, PEKKA_COLOR, MID_GRAY
from src.data.story import SCENES
from src.engine.pixel_art import generate_bar_scene, generate_frank_sprite
from src.engine.animation import RainSystem
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class BarScene(SceneBase):
    SCENE_ID = "ch01_bar"

    def __init__(self):
        super().__init__()
        self.frank_sprites = []

    def setup(self):
        data = SCENES[self.SCENE_ID]
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], WHITE),
            (data["texts"][2], FRANK_COLORS["frank_2"]),
        ]
        self.background = generate_bar_scene()

        # Draw Franks sitting at the bar
        positions = [(120, 218), (240, 218), (360, 218), (480, 218)]
        colors = [WHITE, FRANK_COLORS["frank_2"], FRANK_COLORS["frank_3"], PEKKA_COLOR]
        for pos, color in zip(positions, colors):
            sprite = generate_frank_sprite(color, scale=3)
            self.background.blit(sprite, pos)

        from src.scenes.chapters.ch02_alley import AlleyScene
        from src.scenes.chapters.ch02_dumpster import DumpsterAlleyScene
        from src.scenes.endings import DeathScene, LostScene

        self.choices = [
            (data["choices"][0], AlleyScene()),
            (data["choices"][1], DumpsterAlleyScene()),
            (data["choices"][2], DeathScene("death_bar_raid")),
            (data["choices"][3], None),  # handled in on_choice
        ]
        self._alley = self.choices[0][1]

    def on_choice(self, index):
        if index == 3 and len(self.choices) > 3:
            # Pekka's advice — then go to alley
            self.text_blocks.append(
                ("Pekka looks up from his newspaper. \"The shortest distance "
                 "between two points,\" he says in English, \"is not always "
                 "a straight line. Sometimes it is a drink. But not tonight.\"",
                 PEKKA_COLOR)
            )
            self.current_block = len(self.text_blocks) - 1
            self.scene_manager.renderer.start_typewriter(
                self.text_blocks[-1][0], self.text_blocks[-1][1]
            )
            self.phase = "text"
            self.choices = [
                ("Leave through the front door", self._alley),
            ]
        else:
            super().on_choice(index)
