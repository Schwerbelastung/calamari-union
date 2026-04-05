import random
from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.data.story import SCENES
from src.engine.pixel_art import generate_esplanadi_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class EsplanadiScene(SceneBase):
    SCENE_ID = "ch09_esplanadi"

    def setup(self):
        data = SCENES[self.SCENE_ID]
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_10"]),
            (data["texts"][2], FRANK_COLORS["frank_11"]),
        ]
        self.background = generate_esplanadi_scene()

        sprite10 = generate_frank_sprite(FRANK_COLORS["frank_10"], scale=3)
        sprite11 = generate_frank_sprite(FRANK_COLORS["frank_11"], scale=3)
        self.background.blit(sprite10, (280, 240))
        self.background.blit(sprite11, (330, 240))
        self.meet_frank("frank_10")
        self.meet_frank("frank_11")

        from src.scenes.chapters.ch10_kaivopuisto import KaivopuistoScene
        from src.scenes.endings import LostScene

        self._kaivopuisto = KaivopuistoScene()
        self._lost = LostScene("lost_kamppi")

        self.choices = [
            (data["choices"][0], self._kaivopuisto),
            (data["choices"][1], self._lost),
            (data["choices"][2], None),  # random
        ]

    def on_choice(self, index):
        if index == 2 and len(self.choices) > 2:
            # Following the arguing Franks — semi-random
            seed = len(self.scene_manager.franks_met)
            if seed % 3 != 0:
                self.text_blocks.append(
                    ("The Franks stop arguing and walk south. "
                     "Frank follows. The argument resumes, but quieter now, "
                     "as if the sea is already calming them.",
                     FRANK_COLORS["frank_10"])
                )
                self.current_block = len(self.text_blocks) - 1
                self.scene_manager.renderer.start_typewriter(
                    self.text_blocks[-1][0], self.text_blocks[-1][1]
                )
                self.phase = "text"
                self.choices = [
                    ("Continue south", self._kaivopuisto),
                ]
            else:
                self.text_blocks.append(
                    ("The Franks turn west. \"Shortcut,\" one says. "
                     "The other nods. Frank follows. "
                     "The shortcut leads to Kamppi bus station.",
                     FRANK_COLORS["frank_11"])
                )
                self.current_block = len(self.text_blocks) - 1
                self.scene_manager.renderer.start_typewriter(
                    self.text_blocks[-1][0], self.text_blocks[-1][1]
                )
                self.phase = "text"
                self.choices = [
                    ("...", self._lost),
                ]
        else:
            super().on_choice(index)
